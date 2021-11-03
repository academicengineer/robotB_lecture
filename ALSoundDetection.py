from naoqi import ALProxy

def setOutputVolume(self, volume):
    """Sets the output sound level of the system.
    :param int volume: Volume [0-100].
    """
    if not self.proxy:
        self.proxy = ALProxy("ALAudioDevice")
    return self.proxy.setOutputVolume(volume)

setOutputVolume(2,80)