# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("学習工学を推進するための必要条件、つまり、モデルベースに学習支援システムを作るための条件ですが、かなり処理が複雑になりますので、マシンパワーが必須です。昔は、このようなマシンがなく、できなかったわけですが、最近になって技術が発展してきて複雑な処理も迅速に行えるようになってきています。また、マルチモーダルな入出力であったり、大量のデータが必要です。以上、学習工学のお話でした。今回の講義は、以上になります。お疲れ様でした。")