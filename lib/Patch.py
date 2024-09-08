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
    patch_data = {
      "spec":{
        "replicas": replicas
        }
      }
    patch_json = json.dumps(patch_data)
    command = [
      "kubectl", "-n", namespace, "patch", "deploy", deployment, "--patch", patch_json
    ]
    try: 
      result = subprocess.run(command, check = True, capture_output = True, text = True)
      output = result.stdout.strip()
      print(output)
    except subprocess.CalledProcessError as e:
      print(e.stderr)


  @staticmethod
  def Image(namespace, deployment, image):
    patch_data = {
      "spec":{
        "template":{
          "spec":{
            "containers":[
              {
                "name": deployment,
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

    try: 
      result = subprocess.run(command, check = True, capture_output = True, text = True)
      output = result.stdout.strip()
      print(output)
    except subprocess.CalledProcessError as e:
      print(e.stderr)


  @staticmethod
  def Service(namespace, service, internal = None, external = None):
    if internal is None:    #Set up externalTrafficPolicy
      patch_data_external = {
        "spec":{
          "externalTrafficPolicy": external
          }
        }
      patch_json_external = json.dumps(patch_data_external)
      command = [
      "kubectl", "-n", namespace, "patch", "service", service, "--patch", patch_json_external
      ]
      try: 
        result = subprocess.run(command, check = True, capture_output = True, text = True)
        output = result.stdout.strip()
        print(output)
      except subprocess.CalledProcessError as e:
        print(e.stderr)

    elif external is None:    #Set up internalTrafficPolicy
      patch_data_internal = {
        "spec":{
          "internalTrafficPolicy": internal
          }
        }
      patch_json_internal = json.dumps(patch_data_internal)
      command = [
      "kubectl", "-n", namespace, "patch", "service", service, "--patch", patch_json_internal
      ]
      try: 
        result = subprocess.run(command, check = True, capture_output = True, text = True)
        output = result.stdout.strip()
        print(output)
      except subprocess.CalledProcessError as e:
        print(e.stderr)

    else:                    #Set up externalTrafficPolicy & internalTrafficPolicy
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
      try: 
        result = subprocess.run(command, check = True, capture_output = True, text = True)
        output = result.stdout.strip()
        print(output)
      except subprocess.CalledProcessError as e:
        print(e.stderr)


  @staticmethod
  def NodeSelector(namespace, deployment, *nodes):
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
                          "values": list(nodes) #"node1", "node2", "node3"
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
    try: 
      result = subprocess.run(command, check = True, capture_output = True, text = True)
      output = result.stdout.strip()
      print(output)
    except subprocess.CalledProcessError as e:
      print(e.stderr)
    

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

# Test bellpow

# patch.Replicas("knative-serving", "activator", 3)
# => Done

# patch.Image("default", "curl", "docker.io/rancher/curl")
# patch.Image("default", "curl", "curlimages/curl")
# => Done

# patch.Service("kourier-system", "kourier-internal", internal="Cluster")
# => Vanilla Done

# patch.NodeSelector("knative-serving", "activator", "master-node", "worker01", "worker02")
# Done



