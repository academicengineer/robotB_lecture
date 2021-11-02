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
    motion.post.moveTo(-0.05, 0, 0)
    animatedSpeechProxy.say("PCであるとかスマートフォンであるとかWeb・インターネットであるとか色々な情報を媒介する情報メディアや機器がありますが、")
    animatedSpeechProxy.say("情報メディアの役割、というのは大きく2つに分けることができます。")
    animatedSpeechProxy.say("まず、人間の知性を増幅するという役割、これをインテリジェンスオーグメンテーション、IA、という言い方をします。知性というのはいろいろな側面がありますけども、ここでは学習を取り扱います。")
    animatedSpeechProxy.say("もうひとつのメディアの役割というのは、知性を代行する、ということです。具体的には、道具として人の作業やタスクを代行するということです。こういった知性の代行をアーティフィシャルインテリジェンス、AI、という言い方をします。この講義では両側面やりますが、どちらかというと人間の知性の増幅という方に力点を置いて説明します。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)