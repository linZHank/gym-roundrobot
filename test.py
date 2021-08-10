""" This is an experimental playground"""

import time
import pybullet as p
import pybullet_data

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("plane.urdf")
# startPos = [0,0,0]
# startOrientation = p.getQuaternionFromEuler([0,0,0])
botId = p.loadSDF("model_data/roundrobot.sdf")[0]
nj = p.getNumJoints(botId)
pos, ori = p.getBasePositionAndOrientation(botId)
for wheel in range(p.getNumJoints(botId)):
    p.setJointMotorControl2(botId, wheel, p.VELOCITY_CONTROL, targetVelocity=4, force=500)
    p.getJointInfo(botId, wheel)

# botId = p.loadSDF("/home/linzhank/.local/lib/python3.8/site-packages/pybullet_data/kuka_iiwa/kuka_with_gripper.sdf")
# set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
for i in range(200):
    p.stepSimulation()
    time.sleep(1.0 / 25.0)
#  print(botPos, botOrn)
p.disconnect()
