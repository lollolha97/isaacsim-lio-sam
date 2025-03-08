# todo
## 1. Replace Leatherback to Turtlebot3 or CarterV1
## 2. 

from omni.isaac.core import World
from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.robots import Robot

world = World()

# Ackermann Tutorial Assets
ackermann_usd_path = "omniverse://localhost/NVIDIA/Assets/Isaac/4.5/Isaac/Samples/ROS2/Robots/leatherback_ROS.usd"
ackermann_prim_path = "/World/Ackermann"

# Office Environment Assets
office_usd_path = "omniverse://localhost/NVIDIA/Assets/Isaac/4.5/Isaac/Environments/Office//office.usd"
office_prim_path = "/World/Office"

add_reference_to_stage(ackermann_usd_path, ackermann_prim_path)
add_reference_to_stage(office_usd_path, office_prim_path)

robot = Robot(prim_path=ackermann_usd_path, name="ackermann")
office = Robot(prim_path=office_usd_path, name="office")

world.scene.add(robot)
world.scene.add(office)

# world.reset()