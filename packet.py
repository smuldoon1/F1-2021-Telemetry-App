from struct import *

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
