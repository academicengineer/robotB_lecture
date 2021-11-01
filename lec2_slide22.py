# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("知識工学的には、教育のエキスパートである教育者が用いている知識に着目して、知識ベースを構築することが教育支援システム研究では重要な課題となります。また、学習支援の場合は、上手く学ぶ学習者に着目してその学習者が持っている知識や上手く解くための方法を知識ベース化するのが重要になってきます。学習・教育支援システムの構成を図示すると、このようになります。システムの中に、知識ベースが3つあって、それぞれ、教材知識、教授知識、学習者モデル、に対応し、推論エンジンが、これらの知識ベースを使って学習者とのやりとりを制御します。例えば、筆算の問題解決を支援するシステムの場合。システムは教材知識を使って筆算の問題を解くことができ、また学習者から誤った答えや式が与えられたときにどういう間違いをしたかを診断して学習者モデルを表現し、また学習者の状態に応じてヒントか説明を与えることができます。人間の先生も、同じような知識を用いて学習者の問題解決を支援していると考えることができます。")