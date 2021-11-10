from naoqi import ALProxy

import qi
import argparse
import sys

# Replace "127.0.0.1" with the IP of your robot
leds = ALProxy("ALLeds","127.0.0.1",9559)
# Turn the red LED of the left foot half on
leds.setIntensity("LFoot/Led/Red/Actuator/Value", 0.5)
# Turn the green face LEDs half on
leds.setIntensity("LeftFaceLedsGreen", 0.5)