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



msg.BlueMessage(Count.RunningPod("knative-serving", "activator"))