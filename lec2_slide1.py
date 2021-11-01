# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("皆さん、おはようございます。")
tts.say("今日は学習工学特論の第２回の講義を行います。")
tts.say("今日は学習工学と学習支援システムです。")