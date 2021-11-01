# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("ここでは、少し学習とは何かということについて問い詰めて考えてみたいと思いますが、辞典では、学び習うこととあって、読んで字の如くになってしまうのですが、重要な意味がもう一つあって、以前の経験を土台として、新しい適応の仕方を習得していくこと。つまり、今までに経験してきたことを踏まえて、今の環境にうまく適応していく仕方を学ぶことが学習だといえます。")