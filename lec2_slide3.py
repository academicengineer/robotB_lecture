# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("AIとIAに関わる学術分野を知識工学と呼びます")