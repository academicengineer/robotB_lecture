# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

#names.append("HeadYaw")
#times.append([1.0, 6.0, 7.0])
#keys.append([-1.0, -1.0, 0.0])

#names.append("HeadPitch")
#times.append([1.0, 6.0, 7.0])
#keys.append([0.2, 0.2, 0.0])

# tate
names.append("RElbowRoll")
times.append([1.0, 6.0, 7.0])
keys.append([-0.05, -0.05, 0.5])

#names.append("RHand")
#times.append([1.0, 6.0, 7.0])
#keys.append([1.0, 1.0, 0.0])

names.append("RShoulderRoll")
times.append([1.0, 6.0, 7.0])
keys.append([-1.0, -1.0, 0.0])

try:
  motion = ALProxy("ALMotion", "localhost", 9559)
  motion.setAngles(["HeadYaw", "HeadPitch"], [0.0, 0.0], 0.3)
  motion.post.openHand("RHand")
  motion.setAngles(["HeadYaw", "HeadPitch"], [-0.8, 0.1], 0.3)
  motion.angleInterpolation(names, keys, times, True)
  motion.setAngles(["HeadYaw", "HeadPitch"], [0.0, 0.0], 0.3)
  motion.closeHand("RHand")
except BaseException, err:
   print err
