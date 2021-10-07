from struct import *

class MarshallZone:
    def __init__(self, data):
        self.zoneStart = data[0]
        self.zoneFlag = data[1]

class WeatherForecastSample:
    def __init__(self, data):
        self.sessionType = data[0]
        self.timeOffset = data[1]
        self.weather = data[2]
        self.trackTemperature = data[3]
        self.trackTemperatureChange = data[4]
        self.airTemperature = data[5]
        self.airTemperatureChange = data[6]
        self.rainPercentage = data[7]

class PacketSessionData:
    def __init__(self, packetHeader, data, p):
        self.packetHeader = packetHeader
        sessionData = unpack("<BbbBHBbBHHBBBBBB", data[p:p+19])
        p = p + 19
        self.weather = sessionData[0]
        self.trackTemperature = sessionData[1]
        self.airTemperature = sessionData[2]
        self.totalLaps = sessionData[3]
        self.trackLength = sessionData[4]
        self.sessionType = sessionData[5]
        self.trackID = sessionData[6]
        self.formula = sessionData[7]
        self.sessionTimeLeft = sessionData[8]
        self.sessionDuration = sessionData[9]
        self.pitSpeedLimit = sessionData[10]
        self.gamePaused = sessionData[11]
        self.isSpectating = sessionData[12]
        self.spectatorCarIndex = sessionData[13]
        self.sliProNativeSupport = sessionData[14]
        self.numMarshallZones = sessionData[15]
        self.marshallZones = [None] * 21
        for i in range(21):
            self.marshallZones[i] = unpack("<fb", data[p:p+5])
            p = p + 5
        sessionData = unpack("<BBB", data[p:p+3])
        p = p + 3
        self.safetyCarStatus = sessionData[0]
        self.networkGame = sessionData[1]
        self.numWeatherForecastSamples = sessionData[2]
        self.weatherForecastSamples = [None] * 56
        for i in range(56):
            self.weatherForecastSamples[i] = unpack("<BBBbbbbB", data[p:p+8])
            p = p + 8
        sessionData = unpack("<BBIIIBBBBBBBBBBBB", data[p:p+26])
        p = p + 26
        self.forecastAccuracy = sessionData[0]
        self.aiDifficulty = sessionData[1]
        self.seasonLinkIdentifier = sessionData[2]
        self.weekendLinkIdentifier = sessionData[3]
        self.sessionLinkIdentifier = sessionData[4]
        self.pitStopWindowIdealLap = sessionData[5]
        self.pitStopWindowLatestLap = sessionData[6]
        self.pitStopRejoinPosition = sessionData[7]
        self.steeringAssist = sessionData[8]
        self.brakingAssist = sessionData[9]
        self.gearboxAssist = sessionData[10]
        self.pitAssist = sessionData[11]
        self.pitReleaseAssist = sessionData[12]
        self.ERSAssist = sessionData[13]
        self.DRSAssist = sessionData[14]
        self.dynamicRacingLine = sessionData[15]
        self.dynamicRacingLineType = sessionData[16]
