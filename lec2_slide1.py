#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

'''Say a text with a local configuration'''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motion = ALProxy("ALMotion", "nao.local", 9559)
    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    
    # set the local configuration
    configuration = {"bodyLanguageMode":"contextual"}

    # say the text with the local configuration
    # animatedSpeechProxy.setLanguage("Japanese")
    motion.post.moveTo(0.05, 0, 0)
    animatedSpeechProxy.say("皆さん、こんにちは。")
    animatedSpeechProxy.say("学習工学と学習支援システムということで、今日は概論的なお話をしたいと思います。")
    animatedSpeechProxy.say("この講義では、メディア技術を使って人の学習を支援する、人の知性を高める、人の知性を代行する、という話をします。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)