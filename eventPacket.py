from struct import *

class EventDataDetails:
    def __init__(self, eventStringCode, data):
        self.eventStringCode = eventStringCode
        if eventStringCode == "FTLP":
            self.vehicleIdx = data[0]
            self.lapTime = data[1]
        elif eventStringCode == "RTMT" or eventStringCode == "TMPT" or eventStringCode == "RCWN" or eventStringCode == "DTSV" or eventStringCode == "SGSV":
            self.vehicleIDx = data[0]
        elif eventStringCode == "PENA":
            self.penaltyType = data[0]
            self.infringementType = data[1]
            self.vehicleIdx = data[2]
            self.otherVehicleIdx = data[3]
            self.time = data[4]
            self.lapNum = data[5]
            self.placesGained = data[6]
        elif eventStringCode == "SPTP":
            self.vehicleIdx = data[0]
            self.speed = data[1]
            self.overallFastestInSession = data[2]
            self.driverFastestInSession = data[3]
        elif eventStringCode == "STLG":
            self.numLights = data[0]
        elif eventStringCode == "FLBK":
            self.flashbackFrameIdentifier = data[0]
            self.flashbackSessionTime = data[1]
        elif eventStringCode == "BUTN":
            self.buttonStatus = data[0]

    def __str__(self):
        if self.eventStringCode == "FTLP":
            return "Vehicle Index: " + str(self.vehicleIdx) + "\nLap time: " + str(self.lapTime)
        elif self.eventStringCode == "RTMT" or self.eventStringCode == "TMPT" or self.eventStringCode == "RCWN" or self.eventStringCode == "DTSV" or self.eventStringCode == "SGSV":
            return "Vehicle Index: " + str(self.vehicleIdx)
        elif self.eventStringCode == "PENA":
            return "Penalty: " + str(self.penaltyType) + "\nInfringement: " + str(self.infringementType) + "\nVehicle Index: " + str(self.vehicleIdx) + "\nOther Vehicle Index: " + str(self.otherVehicleIdx) + "\nTime: " + str(self.time) + "\nLap number: " + str(self.lapNum) + "\nPlaces gained: " + str(self.placesGained)
        elif self.eventStringCode == "SPTP":
            return "Vehicle Index: " + str(self.vehicleIdx) + "\nSpeed: " + str(self.speed) + "\nFastest in session: " + str(self.overallFastestInSession) + "\nFastest for driver: " + str(self.driverFastestInSession)
        elif self.eventStringCode == "STLG":
            return "Number of Lights: " + str(self.numLights)
        elif self.eventStringCode == "FLBK":
            return "Frame ID: " + str(self.flashbackFrameIdentifier) + "\nSession Time: " + str(self.flashbackSessionTime)
        elif self.eventStringCode == "BUTN":
            return "Buttons: " + str(self.buttonStatus)

class PacketEventData:
    def __init__(self, packet_header, data, p):
        self.packetHeader = packet_header
        code = unpack("<BBBB", data[p:p+4])
        p = p + 4
        
        self.eventStringCode = "".join([chr(code[0]), chr(code[1]), chr(code[2]), chr(code[3])])
        if self.eventStringCode == "FTLP":                                                              # Fastest lap
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<Bf", data[p:p+5]))
            p = p + 5
        elif self.eventStringCode == "RTMT" or self.eventStringCode == "TMPT" or self.eventStringCode == "RCWN" or self.eventStringCode == "DTSV" or self.eventStringCode == "SGSV":      # Retirement / Team mate in pits / Race winner / Drive-thru penalty served / Stop-go penalty served
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<B", data[p:p+1]))
            p = p + 1
        elif self.eventStringCode == "PENA":                                                            # Penalty
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<BBBBBBB", data[p:p+7]))
            p = p + 7
        elif self.eventStringCode == "SPTP":                                                            # Speed trap
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<BfBB", data[p:p+7]))
            p = p + 7
        elif self.eventStringCode == "STLG":                                                            # Start lights
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<B", data[p:p+1]))
            p = p + 1
        elif self.eventStringCode == "FLBK":                                                            # Flashback
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<If", data[p:p+8]))
            p = p + 8
        elif self.eventStringCode == "BUTN":                                                            # Buttons
            self.eventDetails = EventDataDetails(self.eventStringCode, unpack("<I", data[p:p+4]))
            p = p + 4

    def __str__(self):
        return "Event String Code: " + str(self.eventStringCode) + "\nEvent Details: " + str(self.eventDetails)
