import os
import subprocess
import json

class Patch:

  @staticmethod
  def get(namespace, deployment):
    command = f"kubectl get pods -n {namespace} | grep {deployment}"

    os.system(command)
  
  
  @staticmethod
  def Replicas(namespace, deployment, replicas):
    command = f"""kubectl -n {namespace} patch deploy {deployment} --patch '{{\"spec\":{{\"replicas\":{replicas}}}}}'"""
    patch_data = {
      "spec":{
        "replicas":1
        }
      }
    patch_json = json.dumps(patch_data)
    command = [
      "kubectl", "-n", namespace, "patch", "deploy", deployment, "--patch", patch_json
    ] 
    result = subprocess.run(command, check = True, capture_output = True, text = True)
    output = result.stdout.strip()
    print(output)


  @staticmethod
  def Image(namespace, deployment, image):
    patch_data = {
      "spec":{
        "template":{
          "spec":{
            "containers":[
              {
                "name":"activator",
                "image": image
                }
              ]
            }
          }
        }
      }
    patch_json = json.dumps(patch_data)

    command = [
      "kubectl", "-n", namespace, "patch", "deploy", deployment, "--patch", patch_json
    ]

    result = subprocess.run(command, check = True, capture_output = True, text = True)
    output = result.stdout.strip()
    print(output)


  @staticmethod
  def Service(namespace, service, internal = None, external = None):
    if internal is None:
      patch_data_external = {
        "spec":{
          "externalTrafficPolicy": external
          }
        }
      patch_json_external = json.dumps(patch_data_external)
      command = [
      "kubectl", "-n", namespace, "patch", "service", service, "--patch", patch_json_external
      ]
      result = subprocess.run(command, check = True, capture_output = True, text = True)
      output = result.stdout.strip()
      print(output)

    elif external is None:
      patch_data_internal = {
        "spec":{
          "internalTrafficPolicy": internal
          }
        }
      patch_json_internal = json.dumps(patch_data_internal)
      command = [
      "kubectl", "-n", namespace, "patch", "service", service, "--patch", patch_json_internal
      ]
      result = subprocess.run(command, check = True, capture_output = True, text = True)
      output = result.stdout.strip()
      print(output)

    else:
      patch_data_both = {
        "spec":{
          "internalTrafficPolicy": internal,
          "externalTrafficPolicy": external
          }
        }
      patch_json_both = json.dumps(patch_data_both)
      command = [
      "kubectl", "-n", namespace, "patch", "service", service, "--patch", patch_json_both
      ]
      result = subprocess.run(command, check = True, capture_output = True, text = True)
      output = result.stdout.strip()
      print(output)


  @staticmethod
  def NodeSelector(namespace, deployment, nodes):
    patch_data = {
      "spec":{
        "template":{
          "spec":{
            "affinity":{
              "nodeAffinity":{
                "requiredDuringSchedulingIgnoredDuringExecution":{
                  "nodeSelectorTerms":[
                    {
                      "matchExpressions":[
                        {
                          "key":"kubernetes.io/hostname",
                          "operator":"In",
                          "values":[
                            {nodes} #"node1", "node2", "node3"
                            ]
                          }
                        ]
                      }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    patch_json = json.dumps(patch_data)

    command = [
      "kubectl", "-n", namespace, "patch", "deploy", deployment, "--patch", patch_json
    ]

    result = subprocess.run(command, check = True, capture_output = True, text = True)
    output = result.stdout.strip()
    print(output)
    


  @staticmethod
  def ImagePullPolicy(namespace, deployment, containerName, imagePullPolicy):
    patch_data = {
      "spec":{
        "template":{
          "spec":{
            "containers":[
              {
                "name": {containerName},
                "imagePullPolicy": {imagePullPolicy}
                }
              ]
            }
          }
        }
      }
    patch_json = json.dumps(patch_data)

    command = [
      "kubectl", "-n", namespace, "patch", "deploy", deployment, "--patch", patch_json
    ]

    result = subprocess.run(command, check = True, capture_output = True, text = True)
    output = result.stdout.strip()
    print(output)

    


patch = Patch()

# patch.Replicas("knative-serving", "activator", 3)
patch.Image("default", "curl", "docker.io/rancher/curl")