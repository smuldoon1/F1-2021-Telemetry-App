from struct import *

def BytesToName(nameBytes):
    name = ""
    for i in range(48):
        if nameBytes[i] == 0:
            break
        name = name + chr(nameBytes[i])
    return name

class ParticipantData:
    def __init__(self, data):
        self.aiControlled = data[0]
        self.driverID = data[1]
        self.networkID = data[2]
        self.teamID = data[3]
        self.myTeam = data[4]
        self.raceNumber = data[5]
        self.nationality = data[6]
        self.name = BytesToName(data[7:55])
        self.yourTelemetry = data[55]

class PacketParticipantsData:
    def __init__(self, packetHeader, data, p):
        self.packetHeader = packetHeader
        self.numActiveCars = data[p]
        p = p + 1
        self.participants = [None] * 22
        for i in range(22):
            self.participants[i] = ParticipantData(unpack("<BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", data[p:p+56]))
            p = p + 56
