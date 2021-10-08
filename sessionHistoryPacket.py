from struct import *

class LapHistoryData:
    def __init__(self, data):
        self.lapTime = data[0]
        self.sector1Time = data[1]
        self.sector2Time = data[2]
        self.sector3Time = data[3]
        self.lapValidBitFlags = data[4]

class TyreStintHistoryData:
    def __init__(self, data):
        self.endLap = data[0]
        self.tyreActualCompound = data[1]
        self.tyreVisualCompound = data[2]

class PacketSessionHistoryData:
    def __init__(self, packetHeader, data, p):
        self.packetHeader = packetHeader
        carHistoryData = unpack("<BBBBBBB", data[p:p+7])
        p = p + 7
        self.carIdx = carHistoryData[0]
        self.numLaps = carHistoryData[1]
        self.numTyreStints = carHistoryData[2]
        self.bestLapTimeLapNum = carHistoryData[3]
        self.bestSector1LapNum = carHistoryData[4]
        self.bestSector2LapNum = carHistoryData[5]
        self.bestSector3LapNum = carHistoryData[6]
        self.lapHistoryData = [None] * 100
        for i in range(100):
            self.lapHistoryData[i] = LapHistoryData(unpack("<IHHHB", data[p:p+11]))
            p = p + 11
        self.tyreStintsHistoryData = [None] * 8
        for i in range(8):
            self.tyreStintsHistoryData[i] = TyreStintHistoryData(unpack("<BBB"), data[p:p+3])
            p = p + 3
