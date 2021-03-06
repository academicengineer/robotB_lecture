# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("最後に、学習すると、知識が変化する、という側面があります。コンピューターと違って、学習は単なる知識の蓄積ではないです。計算機に学ばせる場合はだいたい知識をデータとして入れていくわけですが、人間の学習はそれだけじゃないですよね。人間は、単に蓄積した知識を検索しているだけではなく、蓄積した知識そのものを変容させていると考えられます。これを、知識の質的変化、といいます。蓄積した知識を効率よく使えるようになるのは質的変化の一つで、知識がやがてスキルとなっていきます。最初、知識に基づいて考えながらやっていたことが、知識を意識しなくてもできるようなスキルを獲得します。これは知識が変容していると捉えることが出来ます。したがって、学習では、知識の蓄積に加えて、質的な変化が重要だといえます。")