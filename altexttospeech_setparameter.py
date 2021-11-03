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

    names.append("RElbowRoll")
    times.append([0.5, 1.5])
    keys.append([-1.5, -1.5])

    names.append("RHand")
    times.append([1.0, 2.0])
    keys.append([1.0, 0.0])

    names.append("RShoulderPitch")
    times.append([1.0, 2.0])
    keys.append([0.0, 1.1])

    names.append("RShoulderRoll")
    times.append([1.0, 2.0])
    keys.append([1.0, 0.0])

    # Get the service ALTextToSpeech.

    tts = session.service("ALTextToSpeech")
    motion = ALProxy("ALMotion", "nao.local", 9559)

    
    #Applies a pitch shifting to the voice
    tts.setLanguage("Japanese")
    tts.setVolume(0.4)
    tts.setParameter("pitchShift", 0.9) #1.0 - 4
    tts.setParameter("doubleVoice", 1.0) #1.0 - 4
    tts.setParameter("doubleVoiceLevel", 0) #0 - 4
    tts.setParameter("doubleVoiceTimeShift", 0) # 0 - 0.5
    tts.setParameter("speed", 80) #50 - 400
    tts.setParameter("defaultVoiceSpeed", 70) # 50 -400
    tts.setParameter("enableCompression", 0) # 0 or 1

    tts.say("これから学習工学、学習を支援するシステムをお話をしますが、そのベースになっている学問に、知識工学、があります。")
    motion.angleInterpolation(names, keys, times, True)
    tts.say("知識工学は、IAの学問です。この学問が出てきたのが、1980年代なのですが、それ以前の1945年にコンピューターが現れて、その後ほぼ同時期にAIのような考え方が生まれて、コンピューターで人間の知性を代行する研究が始まります。そこからずっとAIの研究が進んで来たわけですが、80年代くらいになってコンピューターでは人間のような知的なことができないということが分かってきます。そこで、コンピューターを使って、AIではなく、IAを実現しようとした最初の学問が知識工学、と呼ばれるものです。")

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
