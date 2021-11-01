# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("これから学習工学、学習を支援するシステムをお話をしますが、そのベースになっている学問に、知識工学、があります。")
tts.say("知識工学は、IAの学問です。この学問が出てきたのが、1980年代なのですが、それ以前の1945年にコンピューターが現れて、その後ほぼ同時期にAIのような考え方が生まれて、コンピューターで人間の知性を代行する研究が始まります。そこからずっとAIの研究が進んで来たわけですが、80年代くらいになってコンピューターでは人間のような知的なことができないということが分かってきます。そこで、コンピューターを使って、AIではなく、IAを実現しようとした最初の学問が知識工学、と呼ばれるものです。")