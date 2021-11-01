# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.5, 2.5])
keys.append([0.2, 0.0])

names.append("HeadYaw")
times.append([0.1])
keys.append([0.0])

names.append("LElbowRoll")
times.append([1.5, 4.0])
keys.append([-1.0, -0.1])

names.append("LElbowYaw")
times.append([1.5, 4.0])
keys.append([-1.0, -1.0])

names.append("LHand")
times.append([1.5, 4.0])
keys.append([1.0, 0.0])

names.append("LShoulderPitch")
times.append([1.5, 4.0])
keys.append([0.7, 1.5])

names.append("LShoulderRoll")
times.append([1.5, 4.0])
keys.append([0.5, 0.0])

names.append("LWristYaw")
times.append([1.5, 4.0])
keys.append([-1.2, 0.0])

names.append("RElbowRoll")
times.append([1.5, 4.0])
keys.append([1.0, 0.1])

names.append("RElbowYaw")
times.append([1.5, 4.0])
keys.append([1.0, 1.0])

names.append("RHand")
times.append([1.5, 4.0])
keys.append([1.0, 0.0])

names.append("RShoulderPitch")
times.append([1.5, 4.0])
keys.append([0.7, 1.5])

names.append("RShoulderRoll")
times.append([1.0, 4.0])
keys.append([-0.5, 0.0])

names.append("RWristYaw")
times.append([1.5, 4.0])
keys.append([1.2, 0.0])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  
  motion = ALProxy("ALMotion", "192.168.1.12", 9559)

  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
   print err