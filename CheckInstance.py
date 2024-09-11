from lib.ColorfulMessage import Message as msg
import os
import subprocess


def AutoDelete(namespace, podname):
  get_pods = subprocess.run(f"""kubectl get pods -n {namespace} | grep {podname} | awk '{{print $1}}'""",
                                 shell=True, capture_output=True, text=True)
  
  pods = get_pods.stdout.strip().split('\n')
  
  for pod in pods:
    subprocess.run(f"kubectl -n {namespace} delete pod {pod}",
                   shell=True, capture_output=True, text=True)
    msg.BlueMessage(f"Pod {pod} deleted!")



class Count:
  @staticmethod
  def TerminatingPod(namespace, podname):
    nTerminatingPod = subprocess.run(f"""kubectl get pods -n {namespace} | grep {podname} | 
                                     grep Terminating | wc -l""",
                                     shell=True, capture_output=True, text=True)
    return int(nTerminatingPod.stdout.strip())

  @staticmethod
  def RunningPod(namespace, podname):
    nRunningPod = subprocess.run(f"""kubectl get pods -n {namespace} | grep {podname} | 
                                 grep Running | wc -l""",
                                 shell=True, capture_output=True, text=True)
    return int(nRunningPod.stdout.strip())
  
  def TotalPod(namespace, podname):
    nTotalPod = subprocess.run(f"""kubectl get pods -n {namespace} | grep {podname} | wc -l""",
                                 shell=True, capture_output=True, text=True)
    return int(nTotalPod.stdout.strip())
  
  @staticmethod
  def TotalNode():
    nTotalNode = subprocess.run(f"""kubectl get nodes | grep Ready | wc -l""",
                                 shell=True, capture_output=True, text=True)
    return int(nTotalNode.stdout.strip())
  

class Wait:
  
  def PodRunning(namespace, podname):
    msg.YellowMessage(f"Waiting for running pods: {podname} ")
    
    INTERVAL_SLEEP_TIME = 5
    os.system(f"sleep {INTERVAL_SLEEP_TIME}")
    
    while True:
      nTotalPods = Count.TotalPod(namespace, podname)
      nRuningPods = Count.RunningPod(namespace, podname)
      if nRuningPods == nTotalPods:
        msg.GreenMessage(f"All {podname} pods are running")
        break
      else:
        os.system(f"sleep {INTERVAL_SLEEP_TIME}")
  
  def PodTerminated(namespace, podname):
    msg.YellowMessage(f"Waiting for terminating pods: {podname} ")
    
    INTERVAL_SLEEP_TIME = 5
    os.system(f"sleep {INTERVAL_SLEEP_TIME}")
    
    while True:
      nTotalPods = Count.TotalPod(namespace, podname)
      if nTotalPods == 0:
        msg.YellowMessage(f"All {podname} pods are deleted")
        break
      else:
        os.system(f"sleep {INTERVAL_SLEEP_TIME}")

  def InPosition(namespace, deployment, *nodes):
    msg.YellowMessage(f"Checking for {deployment}")

    INTERVAL_SLEEP_TIME = 5
    os.system(f"sleep {INTERVAL_SLEEP_TIME}")

    while True:
      nodelist = []
      for node in nodes:
        inNode = subprocess.run(f"""kubectl get pods -n {namespace} -o wide | grep {deployment} | 
                                grep Running | grep {node} | wc -l""",
                                 shell=True, capture_output=True, text=True)
        inNode = int(inNode.stdout.strip())
        nodelist.append(inNode)

      for i in range(len(nodelist)):
        if nodelist[i] > 1:
          msg.RedMessage(f"{deployment}s are not in right position, need to be deleted")
          AutoDelete(namespace, deployment)
          status = "Unready"
        else:
          status = "Ready"

      if status == "Ready":
        msg.GreenMessage(f"{deployment}s are in right position")
        break

  
        

    


# msg.BlueMessage(Count.TotalPod("knative-serving", "activator"))
# WaitPod.Running("default", "hello-00001-deployment")
# WaitPod.Terminated("default", "hello-00001-deployment")

# msg.BlueMessage(Count.TotalNode())


# AutoDelete("default", "hello-00001-deployment")
# Wait.ActivatorInPosition("master-node", "worker01", "worker02")