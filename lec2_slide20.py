# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("まず最初にお話しておきたいのは、教育と学習の違いです。これらは表裏一体ですけども、教育支援と学習支援は少し異なります。教育の場合、登場人物は、教師と学習者の少なくとも２者です。一方、学習の場合、登場人物は,通常、学習者ひとりのみ、です。これが違いのひとつ目になります。もうひとつは、教育では学習者が満たすべき学習のゴールを教師側が設定します。教師がこのゴールを教育ゴールとして想定し、それを満たすために問題やヒントを与えたりします。そして、最終的に学習者は、教師が思い描いているゴールに到達することになります。このゴールが満たされれば、教育支援は達成されたことになります。一方で学習支援では、学習者が学習ゴールを持っています。学習者がこのゴールを満たせるように、支援システムや人間の教員が支援するわけです。このように学習ゴールをどちらが持つかによって、支援システムの果たすべき役割が大きく異なってきます。")