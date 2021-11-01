#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""指さし動作"""

from naoqi import ALProxy
import qi
import argparse
import sys
import time


def main(session):

    # 読み込み
    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # created a walk task
    #motionProxy.moveInit()
    #motionProxy.post.moveTo(0.2, 0.0, 0.1)

    # wait that the move process start running
    #time.sleep(0.1)

    # get robotPosition and nextRobotPosition
    #robotPosition     = motionProxy.getRobotPosition(False)
    #nextRobotPosition = motionProxy.getNextRobotPosition(False)

    # Example showing how to disable left arm motions during a move
    
    proxy = ALProxy("ALMotion", "127.0.0.1", 9559)
    leftArmEnable  = False
    rightArmEnable  = True
    proxy.setMoveArmsEnabled(leftArmEnable, rightArmEnable)
    # disable right arm motion after 10 seconds
    time.sleep(10)
    rightArmEnable  = False
    proxy.setMoveArmsEnabled(leftArmEnable, rightArmEnable)

    # Example showing how to get the enabled flags for the arms
    print 'LeftArmEnabled: ',  proxy.getMoveArmsEnabled("LArm")
    print 'RightArmEnabled: ', proxy.getMoveArmsEnabled("RArm")
    print 'ArmsEnabled: ', proxy.getMoveArmsEnabled("Arms")
    
    # 腕上げる
    #posture_service.goToPosture("StandZero", 0.2)
    
    # 歩行初期化
    #posture_service.goToPosture("StandInit", 1.0)
    
    # 座る
    #posture_service.goToPosture("SitRelax", 1.0)
    
    # 寝そべる
    # posture_service.goToPosture("LyingBelly", 1.0)
    
    # 寝そべりから起き上がる
    #posture_service.goToPosture("LyingBack", 1.0)
    
    # 立ち上がり
    # posture_service.goToPosture("Stand", 1.0)
    
    # しゃがむ
    # posture_service.goToPosture("Crouch", 1.0)
    
    # 座る
    # posture_service.goToPosture("Sit", 1.0)

    # 初期化
    # motion_service.rest()


# ここからは変えない
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
