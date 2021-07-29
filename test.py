import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,0)
# planeId = p.loadURDF("plane.urdf")
startPos = [0,0,0]
startOrientation = p.getQuaternionFromEuler([0,0,0])
botId = p.loadURDF("urdf/roundrobot.urdf",startPos, startOrientation)
#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
# for i in range (3000):
#     p.stepSimulation()
#     time.sleep(1./30.)
# botPos, botOrn = p.getBasePositionAndOrientation(botId)
# print(botPos,botOrn)
# p.disconnect()

