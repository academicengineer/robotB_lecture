#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

'''Say a text with a local configuration'''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    
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


    motion = ALProxy("ALMotion", "nao.local", 9559)
    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    
    # set the local configuration
    configuration = {"bodyLanguageMode":"contextual"}

    # say the text with the local configuration
    # animatedSpeechProxy.setLanguage("Japanese")
    motion.post.moveTo(0.05, 0, 0)
    animatedSpeechProxy.say("これから学習工学、学習を支援するシステムをお話をしますが、そのベースになっている学問に、知識工学、があります。")
    motion.angleInterpolation(names, keys, times, True)
    animatedSpeechProxy.say("知識工学は、IAの学問です。この学問が出てきたのが、1980年代なのですが、それ以前の1945年にコンピューターが現れて、その後ほぼ同時期にAIのような考え方が生まれて、コンピューターで人間の知性を代行する研究が始まります。そこからずっとAIの研究が進んで来たわけですが、80年代くらいになってコンピューターでは人間のような知的なことができないということが分かってきます。そこで、コンピューターを使って、AIではなく、IAを実現しようとした最初の学問が知識工学、と呼ばれるものです。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)