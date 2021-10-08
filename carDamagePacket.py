from struct import *

class CarDamageData:
    def __init__(self, data):
        self.tyresWear = data[0:4]
        self.tyresDamage = data[4:8]
        self.brakesDamage = data[8:12]
        self.frontLeftWingDamage = data[12]
        self.frontRightWingDamage = data[13]
        self.rearWingDamage = data[14]
        self.floorDamage = data[15]
        self.diffuserDamage = data[16]
        self.sidepodDamage = data[17]
        self.drsFault = data[18]
        self.gearBoxDamage = data[19]
        self.engineDamage = data[20]
        self.engineMGUHWear = data[21]
        self.engineESWear = data[22]
        self.engineCEWear = data[23]
        self.engineICEWear = data[24]
        self.engineMGUKWear = data[25]
        self.engineTCWear = data[26]

class PacketCarDamageData:
    def __init__(self, packetHeader, data, p):
        self.packetHeader = packetHeader
        self.carDamageData = [None] * 22
        for i in range(22):
            self.carDamageData[i] = CarDamageData(unpack("<ffffBBBBBBBBBBBBBBBBBBBBBBB", data[p:p+39]))
            p = p + 39
