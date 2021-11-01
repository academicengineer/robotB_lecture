# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("もう一つの学習の本質は、伝承、ということで、ここは教育的な要素も含まれますが、人間は有史以来、種を進化させてきました。自分一代だけでなく、次の世代へ受け継いでいく。これによって。種を進化させてきました。人間は、もともとそういう欲求を持っているとも言えます。この、人から人へ伝える、伝承することが、学ぶということの本質です。")