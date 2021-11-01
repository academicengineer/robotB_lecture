# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("ここからは、学習を支援するのは簡単ではない、ということについてお話していきます。")