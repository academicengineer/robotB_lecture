from naoqi import ALProxy

try:
  audio = ALProxy("ALAudioDevice", "localhost", 9559)
  audio.setOutputVolume(60)
except BaseException, err:
   print err