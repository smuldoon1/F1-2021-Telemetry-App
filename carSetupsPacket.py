from struct import *

class CarSetupData:
    def __init__(self, data):
        self.frontWing = data[0]
        self.rearWing = data[1]
        self.onThrottle = data[2]
        self.offThrottle = data[3]
        self.frontCamber = data[4]
        self.rearCamber = data[5]
        self.frontToe = data[6]
        self.rearToe = data[7]
        self.frontSuspension = data[8]
        self.rearSuspension = data[9]
        self.frontAntiRollBar = data[10]
        self.rearAntiRollBar = data[11]
        self.frontSuspensionHeight = data[12]
        self.rearSuspensionHeight = data[13]
        self.brakePressure = data[14]
        self.brakeBias = data[15]
        self.rearLeftTyrePressure = data[16]
        self.rearRightTyrePressure = data[17]
        self.frontLeftTyrePressure = data[18]
        self.frontRightTyrePressure = data[19]
        self.ballast = data[20]
        self.fuelLoad = data[21]

class PacketCarSetupData:
    def __init__(self, packetHeader, data):
        self.packetHeader = packetHeader
        p = 24
        self.carSetups = [None] * 22
        for i in range(22):
            self.carSetups[i] = CarSetupData(unpack("<BBBBffffBBBBBBBBffffBf", data[p:p+49]))
            p = p + 49
