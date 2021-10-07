from struct import *

class CarMotionData:
    def __init__(self, data):
        self.worldPositionX = data[0]
        self.worldPositionY = data[1]
        self.worldPositionZ = data[2]
        self.worldVelocityX = data[3]
        self.worldVelocityY = data[4]
        self.worldVelocityZ = data[5]
        self.worldForwardDirX = data[6]
        self.worldForwardDirY = data[7]
        self.worldForwardDirZ = data[8]
        self.worldRightDirX = data[9]
        self.worldRightDirY = data[10]
        self.worldRightDirZ = data[11]
        self.gForceLateral = data[12]
        self.gForceLongitudinal = data[13]
        self.gForceVertical = data[14]
        self.yaw = data[15]
        self.pitch = data[16]
        self.roll = data[17]
