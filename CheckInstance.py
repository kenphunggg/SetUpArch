from lib.ColorfulMessage import Message as msg
import os
import subprocess


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
  

class WaitPod:
  
  def Running(namespace, podname):
    msg.YellowMessage(f"Waiting for running pods: {podname} ")
    
    INTERVAL_SLEEP_TIME = 5
    os.system(f"sleep {INTERVAL_SLEEP_TIME}")
    
    while True:
      nTotalPods = Count.TotalPod(namespace, podname)
      nRuningPods = Count.RunningPod(namespace, podname)
      if nRuningPods == nTotalPods:
        msg.YellowMessage(f"All {podname} pods are running")
        break
      else:
        os.system(f"sleep {INTERVAL_SLEEP_TIME}")
  
  def Removed():
    pass



# msg.BlueMessage(Count.TotalPod("knative-serving", "activator"))
WaitPod.Running("knative-serving", "activator")