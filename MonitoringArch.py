from ArchBuilder import (vanila as build_vanilla,
                         proposal as build_proposal)
import os
from lib.ColorfulMessage import Message as msg

def MonitorDefaultEdge():
  msg.GreenMessage("Setting up Vanilla Architecture")
  build_vanilla.edge()

