from struct import *
from nameConversion import *

class LobbyInfoData:
    def __init__(self, data):
        self.aiControlled = data[0]
        self.teamID = data[1]
        self.nationality = data[2]
        self.name = BytesToName(data[3:51])
        self.carNumber = data[51]
        self.readyStatus = data[52]

class PacketLobbyInfoData:
    def __init__(self, packetHeader, data):
        self.packetHeader = packetHeader
        self.numPlayers = data[24]
        p = 25
        self.lobbyPlayers = [None] * 22
        for i in range(22):
            self.lobbyPlayers[i] = LobbyInfoData(unpack("<BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", data[p:p+54]))
            p = p + 54
