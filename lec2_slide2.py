# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("情報メディアの役割は、知性の増幅と知性の代行です。")
tts.say("知性の増幅は、IAと呼ばれております。")
tts.say("一方、知性の代行は、AIと呼ばれております。")