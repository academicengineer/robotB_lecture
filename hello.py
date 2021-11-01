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
    animatedSpeechProxy.say("There is power in the knowledge. これは、有名なファイゲンバームという知識工学の父と呼ばれる方の言葉です。知識こそが巨大な力を持っている。知識にもっと注目して、汎用的なAIではなく、問題領域を反映した専門的な知識をコンピューターの内部に記述して問題を解いたほうが役に立つんだということを言い始めます。ここから知識工学が始まり、1980年代を中心に発展していきます。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)