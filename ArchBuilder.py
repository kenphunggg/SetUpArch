from lib.Patch import Patch as patch


######## Value For Short ########

kourier_system = "kourier-system"
gateway = "3scale-kourier-gateway"
knative_serving = "knative-serving"
activator = "activator"
controller = "controller"
autoscaler = "autoscaler"
net_kourier_controller = "net-kourier-controller"

#################################

class vanila:
  # Vanilla Edge
  @staticmethod
  def edge():
    # Patch Replicas
    patch.Replicas(kourier_system, gateway, 1)
    patch.Replicas(knative_serving, activator, 1)

    # Patch NodeSelector
    patch.NodeSelector(kourier_system, gateway, "worker02")
    patch.NodeSelector(knative_serving, activator, "worker02")

    # Patch Image
    patch.Image("knative-serving", "activator", "activator",
                "gcr.io/knative-releases/knative.dev/serving/cmd/activator@sha256:4cdbe7acc718f55005c0fed4633e9e9feb64f03830132b5dd007e4088a0b2e9f")
    patch.Image("knative-serving", "controller", "controller",
                "gcr.io/knative-releases/knative.dev/serving/cmd/controller@sha256:5d9b948e78bb4f54b602d98e02dedd291689b90295dadab10992f0d9ef2aa1d8")
    patch.Image("knative-serving", "autoscaler", "autoscaler",
                "gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler@sha256:28f45751cac2090019a74ec2801d1f8cd18210ae55159cacd0c9baf74ccc9d7c")
    patch.Image("knative-serving", "net-kourier-controller", "controller",
                "gcr.io/knative-releases/knative.dev/net-kourier/cmd/kourier@sha256:9cd4d69a708a8cf8e597efe3f511494d71cf8eab1b2fd85545097069ad47d3f6")
    # 
    patch.ImagePullPolicy("knative-serving", "activator",
                          containerName="activator", imagePullPolicy="IfNotPresent")
    patch.ImagePullPolicy("knative-serving", "net-kourier-controller",
                          containerName="controller", imagePullPolicy="IfNotPresent")
    
    # Patch Service
    patch.Service("kourier-system", "kourier", 
                  internal="Cluster", external="Cluster")
    patch.Service("kourier-system", "kourier-internal",
                  internal="Cluster")

  # Vanilla Cloud
  @staticmethod
  def cloud():
    # Patch Replicas
    patch.Replicas(kourier_system, gateway, 1)
    patch.Replicas(knative_serving, activator, 1)

    # Patch NodeSelector
    patch.NodeSelector(kourier_system, gateway, "master-node", "worker01")
    patch.NodeSelector(knative_serving, activator, "master-node", "worker01")

    # Patch Image
    patch.Image("knative-serving", "activator", "activator",
                "gcr.io/knative-releases/knative.dev/serving/cmd/activator@sha256:4cdbe7acc718f55005c0fed4633e9e9feb64f03830132b5dd007e4088a0b2e9f")
    patch.Image("knative-serving", "controller", "controller",
                "gcr.io/knative-releases/knative.dev/serving/cmd/controller@sha256:5d9b948e78bb4f54b602d98e02dedd291689b90295dadab10992f0d9ef2aa1d8")
    patch.Image("knative-serving", "autoscaler", "autoscaler",
                "gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler@sha256:28f45751cac2090019a74ec2801d1f8cd18210ae55159cacd0c9baf74ccc9d7c")
    patch.Image("knative-serving", "net-kourier-controller", "controller",
                "gcr.io/knative-releases/knative.dev/net-kourier/cmd/kourier@sha256:9cd4d69a708a8cf8e597efe3f511494d71cf8eab1b2fd85545097069ad47d3f6")
    # 
    patch.ImagePullPolicy("knative-serving", "activator",
                          containerName="activator", imagePullPolicy="IfNotPresent")
    patch.ImagePullPolicy("knative-serving", "net-kourier-controller",
                          containerName="controller", imagePullPolicy="IfNotPresent")
    
    # Patch Service
    patch.Service("kourier-system", "kourier", 
                  internal="Cluster", external="Cluster")
    patch.Service("kourier-system", "kourier-internal",
                  internal="Cluster")
    
  @staticmethod
  def cloudPlus(tag):
    # Patch Replicas
    patch.Replicas(kourier_system, gateway, 1)
    patch.Replicas(knative_serving, activator, 1)

    # Patch NodeSelector
    patch.NodeSelector(kourier_system, gateway, "master-node", "worker01")
    patch.NodeSelector(knative_serving, activator, "master-node", "worker01")

    # Patch Image
    patch.Image("knative-serving", "activator", "activator",
                "gcr.io/knative-releases/knative.dev/serving/cmd/activator@sha256:4cdbe7acc718f55005c0fed4633e9e9feb64f03830132b5dd007e4088a0b2e9f")
    patch.Image("knative-serving", "controller", "controller",
                f"docker.io/bonavadeur/ikukantai-controller:{tag}")
    patch.Image("knative-serving", "autoscaler", "autoscaler",
                "gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler@sha256:28f45751cac2090019a74ec2801d1f8cd18210ae55159cacd0c9baf74ccc9d7c")
    patch.Image("knative-serving", "net-kourier-controller", "controller",
                "gcr.io/knative-releases/knative.dev/net-kourier/cmd/kourier@sha256:9cd4d69a708a8cf8e597efe3f511494d71cf8eab1b2fd85545097069ad47d3f6")
    # 
    patch.ImagePullPolicy("knative-serving", "activator",
                          containerName="activator", imagePullPolicy="IfNotPresent")
    patch.ImagePullPolicy("knative-serving", "net-kourier-controller",
                          containerName="controller", imagePullPolicy="IfNotPresent")
    
    # Patch Service
    patch.Service("kourier-system", "kourier", 
                  internal="Cluster", external="Cluster")
    patch.Service("kourier-system", "kourier-internal",
                  internal="Cluster")

class proposal:  # Ikukantai

  @staticmethod
  def dev_remote(tag):
    # Patch Replicas
    patch.Replicas("kourier-system", "3scale-kourier-gateway", 3)
    patch.Replicas("knative-serving", "activator", 3)

    # Patch NodeSelector
    patch.NodeSelector("kourier-system", "3scale-kourier-gateway", "master-node", "worker01", "worker02")
    patch.NodeSelector("knative-serving", "activator", "master-node", "worker01", "worker02")

    # Patch Image
    patch.Image("knative-serving", "activator", "activator",
                f"docker.io/bonavadeur/ikukantai-activator:{tag}") #
    patch.Image("knative-serving", "controller", "controller",
                f"docker.io/bonavadeur/ikukantai-controller:{tag}")
    patch.Image("knative-serving", "autoscaler", "autoscaler",
                f"docker.io/bonavadeur/ikukantai-autoscaler:{tag}")
    patch.Image("knative-serving", "net-kourier-controller", "controller",
                f"docker.io/bonavadeur/ikukantai-kourier:{tag}")
    patch.ImagePullPolicy("knative-serving", "activator",
                          containerName="activator", imagePullPolicy="Always")  # Use for setup testbed
    patch.ImagePullPolicy("knative-serving", "net-kourier-controller",
                          containerName="controller", imagePullPolicy="Always") # Use for setup testbed
    
    # Patch Service
    patch.Service(kourier_system, "kourier",
                  internal="Local", external="Local")
    patch.Service(kourier_system, "kourier-internal",
                  internal="Local")

  @staticmethod
  def dev_local(tag):
    # Patch Replicas
    patch.Replicas(kourier_system, gateway, 3)
    patch.Replicas(knative_serving, activator, 3)

    # Patch NodeSelector
    patch.NodeSelector(kourier_system, gateway, "master-node", "worker01", "worker02")
    patch.NodeSelector(knative_serving, activator, "master-node", "worker01", "worker02")

    # Patch Image
    patch.Image(knative_serving, activator,
                f"docker.io/bonavadeur/ikukantai-activator:{tag}")
    patch.Image(knative_serving, controller,
                f"docker.io/bonavadeur/ikukantai-controller:{tag}")
    patch.Image(knative_serving, autoscaler,
                f"docker.io/bonavadeur/ikukantai-autoscaler:{tag}")
    patch.Image(knative_serving, net_kourier_controller,
                f"docker.io/bonavadeur/ikukantai-kourier:{tag}")
    patch.ImagePullPolicy(knative_serving, activator,
                          containerName=activator, imagePullPolicy="IfNotPresent")  # Use for developer
    patch.ImagePullPolicy(knative_serving, net_kourier_controller,
                          containerName=controller, imagePullPolicy="IfNotPresent") # Use for developer
    
    # Patch Service
    patch.Service(kourier_system, "kourier",
                  internal="Local", external="Local")
    patch.Service(kourier_system, "kourier-internal",
                  internal="Local")
    
class function:
  def in_cloud():
    patch.NodeSelector("default", "hello-00001-deployment", "master-node", "worker01")

  def in_edge():
    patch.NodeSelector("default", "hello-00001-deployment", "worker02")

  def in_both():
    patch.NodeSelector("default", "hello-00001-deployment", "master-node", "worker01", "worker02")