from naoqi import ALProxy

try:
  audio = ALProxy("ALAudioDevice", "localhost", 9559)
  audiio.getOutputVolume（30）
except BaseException, err:
   print err