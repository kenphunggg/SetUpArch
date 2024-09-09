from ArchBuilder import (vanila as build_vanilla,
                         proposal as build_proposal)
import os
from lib.ColorfulMessage import Message as msg
from CheckInstance import WaitPod 

def MonitorDefaultEdge():
  msg.GreenMessage("Setting up Vanilla Architecture")
  build_vanilla.edge()

class SetUpVanilla:
  def edge():
    msg.GreenMessage("Setting up Vanilla Edge Architecture")
    build_vanilla.edge()
    WaitPod.Running("knative-serving", "activator")
    WaitPod.Running("knative-serving", "controller")
    WaitPod.Running("knative-serving", "autoscaler")
    WaitPod.Running("knative-serving", "net-kourier-controller")
    WaitPod.Running("kourier-system", "3scale-kourier-gateway")
    msg.GreenMessage("All pods are running")


  def cloud():
    pass

