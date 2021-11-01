# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("一方、モデルベースでは、どう問題解決するのか、どう学習するのか、あるいはどう教えるのかというのを解き明かしながら知識ベースを構築します。したがって、上手くいかない場合に対して、なぜうまくいかなかったのかを説明することが可能となります。")