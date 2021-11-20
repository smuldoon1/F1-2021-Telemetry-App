from struct import *

class FinalClassificationData:
    def __init__(self, data):
        self.position = data[0]
        self.numLaps = data[1]
        self.gridPosition = data[2]
        self.points = data[3]
        self.numPitStops = data[4]
        self.resultStatus = data[5]
        self.bestLapTime = data[6]
        self.totalRaceTime = data[7]
        self.penaltiesTime = data[8]
        self.numPenalties = data[9]
        self.numTyreStints = data[10]
        self.tyreStintsActual = data[11:19]
        self.tyreStintsVisual = data[19:27]

class PacketFinalClassificationData:
    def __init__(self, packetHeader, data):
        self.packetHeader = packetHeader
        self.numCars = data[24]
        p = 25
        self.classificationData = [None] * 22
        for i in range(22):
            self.classificationData[i] = FinalClassificationData(unpack("<BBBBBBIdBBBBBBBBBBBBBBBBBBB", data[p:p+37]))
            p = p + 37
