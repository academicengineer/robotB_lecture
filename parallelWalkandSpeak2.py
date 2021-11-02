from naoqi import ALProxy
motion = ALProxy("ALMotion", "nao.local", 9559)
motion.moveInit()
id = motion.post.moveTo(0.5, 0, 0)
motion.wait(id, 0)