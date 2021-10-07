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

class PacketMotionData:
    def __init__(self, packetHeader, data, p):
        self.packetHeader = packetHeader
        self.carMotionData = [None] * 22
        for i in range(22):
            self.carMotionData[i] = CarMotionData(unpack("<ffffffhhhhhhffffff", data[p:p+60]))
            p = p + 60
        additionalData = unpack("<ffffffffffffffffffffffffffffff", data[p:p+120])
        p = p + 120
        self.suspensionPosition = additionalData[0:4]
        self.suspensionVelocity = additionalData[4:8]
        self.suspensionAcceleration = additionalData[8:12]
        self.wheelSpeed = additionalData[12:16]
        self.wheelSlip = additionalData[16:20]
        self.localVelocityX = additionalData[20]
        self.localVelocityY = additionalData[21]
        self.localVelocityZ = additionalData[22]
        self.angularVelocityX = additionalData[23]
        self.angularVelocityY = additionalData[24]
        self.angularVelocityZ = additionalData[25]
        self.angularAccelerationX = additionalData[26]
        self.angularAccelerationY = additionalData[27]
        self.angularAccelerationZ = additionalData[28]
        self.frontWheelsAngle = additionalData[29]
