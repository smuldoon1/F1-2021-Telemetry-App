from struct import *

class CarTelemetryData:
    def __init__(self, data):
        self.speed = data[0]
        self.throttle = data[1]
        self.steer = data[2]
        self.brake = data[3]
        self.clutch = data[4]
        self.gear = data[5]
        self.engineRPM = data[6]
        self.drs = data[7]
        self.revLightsPercent = data[8]
        self.revLightsBitValue = data[9]
        self.brakesTemperature = data[10:14]
        self.tyresSurfaceTemperature = data[14:18]
        self.tyresInnerTemperature = data[18:22]
        self.engineTemperature = data[22]
        self.tyresPressure = data[23:27]
        self.surfaceType = data[27:31]

class PacketCarTelemetryData:
    def __init__(self, packetHeader, data):
        self.packetHeader = packetHeader
        p = 24
        self.carTelemetryData = [None] * 22
        for i in range(22):
            self.carTelemetryData[i] = CarTelemetryData(unpack("<HfffBbHBBHHHHHBBBBBBBBHffffBBBB", data[p:p+60]))
            p = p + 60
        mfdData = unpack("<BBb", data[p:p+3])
        p = p + 3
        self.mfdPanelIndex = mfdData[0]
        self.mfdPanelIndexSecondaryPlayer = mfdData[1]
        self.suggestedGear = mfdData[2]
