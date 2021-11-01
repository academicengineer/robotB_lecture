# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("では、次に、学習、教育を支援するシステムにテーマを移していきます。学習支援システムというのはエキスパートシステムのひとつです。")