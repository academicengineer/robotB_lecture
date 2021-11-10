from naoqi import ALProxy

import qi
import argparse
import sys

# Replace "127.0.0.1" with the IP of your robot
leds = ALProxy("ALLeds","127.0.0.1",9559)
# Turn the red LED of the left foot half on
leds.setIntensity("LFoot/Led/Red/Actuator/Value", 0.8)
leds.setIntensity("RFoot/Led/Blue/Actuator/Value", 0.8)

# Turn the green face LEDs half on
leds.setIntensity("LeftFaceLedsRed", 0.1)
leds.setIntensity("LeftFaceLedsGreen", 0.8)
leds.setIntensity("LeftFaceLedsBlue", 0.1)

leds.setIntensity("RightFaceLedsRed", 0.8)
leds.setIntensity("RightFaceLedsGreen", 0.1)
leds.setIntensity("RightFaceLedsBlue", 0.1)