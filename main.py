from ArchBuilder import (vanila as build_vanilla,
                         proposal as build_proposal,
                         function as build_function)
import sys
from lib.ColorfulMessage import Message as msg
from CheckInstance import Wait 


def defaultCustom():
  msg.GreenMessage("Setting up Default Custom Architecture")
  build_vanilla.edge()
  Wait.PodRunning("knative-serving", "activator")
  Wait.PodRunning("knative-serving", "controller")
  Wait.PodRunning("knative-serving", "autoscaler")
  Wait.PodRunning("knative-serving", "net-kourier-controller")
  Wait.PodRunning("kourier-system", "3scale-kourier-gateway")
  msg.GreenMessage("All pods are running")


def default():
  msg.GreenMessage("Setting up Default Architecture")
  build_vanilla.cloud()
  Wait.PodRunning("knative-serving", "activator")
  Wait.PodRunning("knative-serving", "controller")
  Wait.PodRunning("knative-serving", "autoscaler")
  Wait.PodRunning("knative-serving", "net-kourier-controller")
  Wait.PodRunning("kourier-system", "3scale-kourier-gateway")
  msg.GreenMessage("All pods are running")

def defaultPlus():
  msg.GreenMessage("Setting up Default Plus Architecture")
  build_vanilla.cloudPlus(tag="v1.2-cnsm-15nov24")
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

def fxInCloud():
  build_function.in_cloud()

def fxInEdge():
  build_function.in_edge()

def fxIkukantai():
  build_function.in_both()

if __name__ == "__main__":
    args = sys.argv
    globals()[args[1]](*args[2:])