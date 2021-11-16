from struct import *

class LapData:
    def __init__(self, data):
        self.lastLapTime = data[0]
        self.currentLapTime = data[1]
        self.sector1Time = data[2]
        self.sector2Time = data[3]
        self.lapDistance = data[4]
        self.totalDistance = data[5]
        self.safetyCarDelta = data[6]
        self.carPosition = data[7]
        self.currentLapNum = data[8]
        self.pitStatus = data[9]
        self.numPitStops = data[10]
        self.sector = data[11]
        self.currentLapInvalid = data[12]
        self.penalties = data[13]
        self.warnings = data[14]
        self.numUnservedDriveThroughPens = data[15]
        self.numUnservedStopGoPens = data[16]
        self.gridPosition = data[17]
        self.driverStatus = data[18]
        self.resultStatus = data[19]
        self.pitLaneTimerActive = data[20]
        self.pitLaneTimeInLane = data[21]
        self.pitLaneTime = data[22]
        self.pitStopShouldServePen = data[23]

class PacketLapData:
    def __init__(self, packetHeader, data):
        self.packetHeader = packetHeader
        p = 24
        self.lapData = [None] * 22
        for i in range(22):
            self.lapData[i] = LapData(unpack("<IIHHfffBBBBBBBBBBBBBBHHB", data[p:p+43]))
            p = p + 43
