# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("テクノロジーベースのシステムデザインでは、基本的に、技術を導入して、今ある教育を効率化する、あるいは同様の教育を提供することが指向されます。つまり、教室における教育活動を技術で代替することが主眼となります。学習効果は上がりますが、上手くいかない場合、なぜ上手く行かなかったのか、何が起こっているのか、という分析が難しく、システムの保守が困難という短所があります。技術を与えて環境を作るだけでは単なる電子化になってしまいます。")