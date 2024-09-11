from ArchBuilder import (vanila as build_vanilla,
                         proposal as build_proposal)
import sys
from lib.ColorfulMessage import Message as msg
from CheckInstance import Wait 


def vanilla_edge():
  msg.GreenMessage("Setting up Vanilla Edge Architecture")
  build_vanilla.edge()
  Wait.PodRunning("knative-serving", "activator")
  Wait.PodRunning("knative-serving", "controller")
  Wait.PodRunning("knative-serving", "autoscaler")
  Wait.PodRunning("knative-serving", "net-kourier-controller")
  Wait.PodRunning("kourier-system", "3scale-kourier-gateway")
  msg.GreenMessage("All pods are running")


def vanilla_cloud():
  msg.GreenMessage("Setting up Vanilla Cloud Architecture")
  build_vanilla.cloud()
  Wait.PodRunning("knative-serving", "activator")
  Wait.PodRunning("knative-serving", "controller")
  Wait.PodRunning("knative-serving", "autoscaler")
  Wait.PodRunning("knative-serving", "net-kourier-controller")
  Wait.PodRunning("kourier-system", "3scale-kourier-gateway")
  msg.GreenMessage("All pods are running")

def proposal():
  msg.GreenMessage("Setting up Ikukantai Architecture")
  build_proposal.dev_remote(tag="v1.2-cnsm-15nov24")
  Wait.PodRunning("knative-serving", "activator")
  Wait.PodRunning("knative-serving", "controller")
  Wait.PodRunning("knative-serving", "autoscaler")
  Wait.PodRunning("knative-serving", "net-kourier-controller")
  Wait.PodRunning("kourier-system", "3scale-kourier-gateway")
  msg.GreenMessage("All pods are running")
  Wait.InPosition("knative-serving", "activator", "Master-node", "Worker01", "Worker02")
  Wait.InPosition("kourier-system", "3scale-kourier-gateway", "Master-node", "Worker01", "Worker02")

if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])