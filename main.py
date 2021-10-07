import socket
from struct import *

UDP_IP = "0.0.0.0"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

p = 0

class PacketHeader:
    def __init__(self, data):
        self.packetFormat = data[0]             # Year (2021)
        self.gameMajorVersion = data[1]         # Game major version "X.00"
        self.gameMinorVersion = data[2]         # Game minor version "1.XX"
        self.packetVersion = data[3]            # Packet version (1)
        self.packetID = data[4]                 # Packet ID, 0 - 11
        self.sessionUID = data[5]               # Unique session id
        self.sessionTime = data[6]              # Session timestamp
        self.frameIdentifier = data[7]          # Frame id
        self.playerCarIndex = data[8]           # Player car index
        self.secondaryPlayerCarIndex = data[9]  # Splitscreen 2nd player car index, 255 if null

    def __str__(self):
        return "Packet Format: " + str(self.packetFormat) + "\nGame Version: " + str(self.gameMajorVersion) + "." + str(self.gameMinorVersion) + "\nPacket Version: " + str(self.packetVersion) + "\nPacket ID: " + str(self.packetID) + "\nSession UID: " + str(self.sessionUID) + "\nSession time: " + str(self.sessionTime) + "\nFrame ID: " + str(self.frameIdentifier) + "\nPlayer Car Index: " + str(self.playerCarIndex) + "\n2nd Player Car Index: " + str(self.secondaryPlayerCarIndex)

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
    def __init__(self, packet_header, data):
        global p
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

def UnpackData(data):
    global p
    packet_header = PacketHeader(unpack("<HBBBBQfIBB", data[p:p+24]))
    p = p + 24
    if packet_header.packetID == 3:
        packet_event_data = PacketEventData(packet_header, data)
        print(packet_event_data)

i = 0
while i > -10:
    p = 0
    data, address = sock.recvfrom(1464)
    UnpackData(data)
    i = i + 1
