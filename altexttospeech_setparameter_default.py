#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use setParameter Method"""
from naoqi import ALProxy
import qi
import argparse
import sys


def main(session):
    """
    This example uses the setParameter method.
    It sets the pitchShift to use in the module.
    """

    names = list()
    times = list()
    keys = list()

    names.append("HeadYaw")
    times.append([0.5, 1.0, 2.0])
    keys.append([0.5, 1.0, 0.0])

    names.append("LElbowRoll")
    times.append([0.5, 1.5])
    keys.append([-1.5, -1.5])

    names.append("LHand")
    times.append([1.0, 2.0])
    keys.append([1.0, 0.0])

    names.append("LShoulderPitch")
    times.append([1.0, 2.0])
    keys.append([0.0, 1.1])

    names.append("LShoulderRoll")
    times.append([1.0, 2.0])
    keys.append([1.0, 0.0])

    # Get the service ALTextToSpeech.

    tts = session.service("ALTextToSpeech")
    motion = ALProxy("ALMotion", "nao.local", 9559)
    
    #Applies a pitch shifting to the voice
    tts.setLanguage("Japanese")
    tts.setVolume(0.9) #0.0 - 1.0音量
    tts.setParameter("pitchShift", 1.0) #1.0 - 4 #ピッチ
    tts.setParameter("doubleVoice", 1.0) #1.0 - 4
    tts.setParameter("doubleVoiceLevel", 0) #0 - 4
    tts.setParameter("doubleVoiceTimeShift", 0) # 0 - 0.5
    tts.setParameter("speed", 100) #50 - 400 # スピード
    tts.setParameter("defaultVoiceSpeed", 50) # 50 -400
    tts.setParameter("enableCompression", 0) # 0 or 1
    tts.say("知識工学の誕生は1960年代後半で、1980年代から盛んになってきました。AIとの対比でいうと、当初AIは今とは少し違って汎用的な問題解決を目指していました。定理証明とか、どんな問題でもとけるような問題解決器を作ることが指向されてきました。当然ながら、コンピューターというのはアルゴリズムで動くわけなので事前に手続きを用意して問題を解くわけですが、プリミティブなオペレーションから複雑な問題を解くことにトライしてきた学問といえます。しかし、解き方を事前に与えておかなければいけません。そういう意味で、実際に解ける問題というのは現実にあるような問題ではなくてかなり制約を与えた問題になります。この制約を与えた範囲では計算機は人間と同じあるいはそれ以上に問題を解くことができるということが60年代70年代に示されてくるわけですが、それを、実社会の問題に応用しようとすると、途端に解けない、ということが起こります。そこで登場してくるのが、エキスパートシステム、と呼ばれる知識工学の発端になるものです。汎用的に問題を解くメカニズムを作るのは大変なのですが、そうではなくて人間のエキスパートが持っているような知識をコンピューター上に詰め込んで、その知識を使って問題解決を図ろうとするものです。人間の持っている知識を知識ベースとして記述していけばジツモンダイを解けるわけですが、一方で汎用的に問題を解くことはできなくなります。何故かと言うと、知識が領域に特化したものとなっていますので、解ける領域は当然限定的です。ただ限定的ではあるものの実社会の問題を解けるようなシステムを計算機上に実現できるようになります。つまり、人間と同じように汎用的に問題を解くことを諦めて、問題領域をトッカしてもいいから知識を使って問題解決しよう、という考え方が生まれます。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
