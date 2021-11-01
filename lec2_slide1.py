# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("皆さん、こんにちは。")
tts.say("学習工学と学習支援システムということで、今日は概論的なお話をしたいと思います。")
tts.say("この講義では、メディア技術を使って人の学習を支援する、人の知性を高める、人の知性を代行する、という話をします。")