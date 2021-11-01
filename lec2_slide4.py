#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

'''Say a text with a local configuration'''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    
    # set the local configuration
    configuration = {"bodyLanguageMode":"contextual"}

    # say the text with the local configuration
    # animatedSpeechProxy.setLanguage("Japanese")
    animatedSpeechProxy.say("知識工学の誕生は1960年代後半で、1980年代から盛んになってきました。AIとの対比でいうと、当初AIは今とは少し違って汎用的な問題解決を目指していました。定理証明とか、どんな問題でもとけるような問題解決器を作ることが指向されてきました。当然ながら、コンピューターというのはアルゴリズムで動くわけなので事前に手続きを用意して問題を解くわけですが、プリミティブなオペレーションから複雑な問題を解くことにトライしてきた学問といえます。しかし、解き方を事前に与えておかなければいけません。そういう意味で、実際に解ける問題というのは現実にあるような問題ではなくてかなり制約を与えた問題になります。この制約を与えた範囲では計算機は人間と同じあるいはそれ以上に問題を解くことができるということが60年代70年代に示されてくるわけですが、それを、実社会の問題に応用しようとすると、途端に解けない、ということが起こります。そこで登場してくるのが、エキスパートシステム、と呼ばれる知識工学の発端になるものです。汎用的に問題を解くメカニズムを作るのは大変なのですが、そうではなくて人間のエキスパートが持っているような知識をコンピューター上に詰め込んで、その知識を使って問題解決を図ろうとするものです。人間の持っている知識を知識ベースとして記述していけばジツモンダイを解けるわけですが、一方で汎用的に問題を解くことはできなくなります。何故かと言うと、知識が領域に特化したものとなっていますので、解ける領域は当然限定的です。ただ限定的ではあるものの実社会の問題を解けるようなシステムを計算機上に実現できるようになります。つまり、人間と同じように汎用的に問題を解くことを諦めて、問題領域をトッカしてもいいから知識を使って問題解決しよう、という考え方が生まれます。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)