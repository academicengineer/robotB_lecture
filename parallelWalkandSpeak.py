from naoqi import ALProxy
motion = ALProxy("ALMotion", "nao.local", 9559)
tts    = ALProxy("ALTextToSpeech", "nao.local", 9559)
#motion.moveInit()
motion.post.moveTo(0.05, 0, 0)
tts.say("I'm walking")