# coding: UTF-8

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "localhost", 9559)
tts.setLanguage("Japanese")
tts.say("次に、学習には、レベルという側面、があり、意識的に学んでいることと、無意識に学んでいることがあると思います。普通、学習と言うと、意識レベル、のほうを考えがちで、学校での学びはおおむねこちらにあたります。意識して学ぶものとしては、思考や知識があります。これらは、説明可能です。一方、人間は無意識に学んでいるもの、があります。なかなか口に出して説明するのが難しく、神経レベルや筋肉レベルで学んでいること、身体知と言ったりもします。では、どちらのレベルの学習が支援可能なのかといいますと、無意識のレベルで学習することを促すということはできますが、明確に支援できるのは、意識レベルの学習、です。知識工学で扱っているのはまさに意識レベルの学習になります。")