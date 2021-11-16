from struct import *

class CarStatusData:
    def __init__(self, data):
        self.tractionControl = data[0]
        self.antiLockBrakes = data[1]
        self.fuelMix = data[2]
        self.frontBrakeBias = data[3]
        self.pitLimiterStatus = data[4]
        self.fuelInTank = data[5]
        self.fuelCapacity = data[6]
        self.fuelRemainingLaps = data[7]
        self.maxRPM = data[8]
        self.idleRPM = data[9]
        self.maxGears = data[10]
        self.drsAllowed = data[11]
        self.drsActivationDistance = data[12]
        self.actualTyreCompound = data[13]
        self.visualTyreCompound = data[14]
        self.tyresAgeLaps = data[15]
        self.vehicleFiaFlags = data[16]
        self.ersStoreEnergy = data[17]
        self.ersDeployMode = data[18]
        self.ersHarvestedThisLapMGUK = data[19]
        self.ersHarvestedThisLapMGUH = data[20]
        self.ersDeployedThisLap = data[21]
        self.networkPaused = data[22]

class PacketCarStatusData:
    def __init__(self, packetHeader, data):
        self.packetHeader = packetHeader
        p = 24
        self.carStatusData = [None] * 22
        for i in range(22):
            self.carStatusData[i] = CarStatusData(unpack("<BBBBBfffHHBBHBBBbfBfffB", data[p:p+47]))
            p = p + 47
