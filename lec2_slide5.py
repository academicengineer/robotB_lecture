# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("There is power in the knowledge. これは、有名なファイゲンバームという知識工学の父と呼ばれる方の言葉です。知識こそが巨大な力を持っている。知識にもっと注目して、汎用的なAIではなく、問題領域を反映した専門的な知識をコンピューターの内部に記述して問題を解いたほうが役に立つんだということを言い始めます。ここから知識工学が始まり、1980年代を中心に発展していきます。")