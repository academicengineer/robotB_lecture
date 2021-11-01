# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("知識工学の誕生は、1960年代後半です")
tts.say("当時、AIは、汎用的な問題解決、定理証明などを志向しており、実社会の問題に寄与できるか？という問いの研究が行われてきました")
tts.say("当時の代表的なシステムとして、エキスパートシステムがあり、特定の問題領域に対する解決を指向していました")