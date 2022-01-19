import socket
import select
from struct import *

from packet import *
from motionPacket import *
from sessionPacket import *
from lapPacket import *
from eventPacket import *
from participantsPacket import *
from carSetupsPacket import *
from carTelemetryPacket import *
from carStatusPacket import *
from finalClassificationPacket import *
from lobbyInfoPacket import *
from carDamagePacket import *
from sessionHistoryPacket import *

UDP_IP = "0.0.0.0"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
#sock.setblocking(0)

#p = 0   # Unpacking index, keeps track of where in the data the next byte should be unpacked from

def UnpackData(data):
    packetHeader = PacketHeader(unpack("<HBBBBQfIBB", data[0:24]))
    if packetHeader.packetID == 0:
        return PacketMotionData(packetHeader, data)
    elif packetHeader.packetID == 1:
        return PacketSessionData(packetHeader, data)
    elif packetHeader.packetID == 2:
        return PacketLapData(packetHeader, data)
    elif packetHeader.packetID == 3:
        return PacketEventData(packetHeader, data)
    elif packetHeader.packetID == 4:
        return PacketParticipantsData(packetHeader, data)
    elif packetHeader.packetID == 5:
        return PacketCarSetupData(packetHeader, data)
    elif packetHeader.packetID == 6:
        return PacketCarTelemetryData(packetHeader, data)
    elif packetHeader.packetID == 7:
        return PacketCarStatusData(packetHeader, data)
    elif packetHeader.packetID == 8:
        return PacketFinalClassificationData(packetHeader, data)
    elif packetHeader.packetID == 9:
        return PacketLobbyInfoData(packetHeader, data)
    elif packetHeader.packetID == 10:
        return PacketCarDamageData(packetHeader, data)
    elif packetHeader.packetID == 11:
        return PacketSessionHistoryData(packetHeader, data)

def RetrievePacket():
    #ready = select.select([sock], [], [], 0.1)
    #if ready[0]:
        data, address = sock.recvfrom(1464)
        return UnpackData(data)
    #return None

'''
def RetrievePacket(packetType):
    data, address = sock.recvfrom(1464)
    packet = UnpackData(data)
    if packet.packetHeader.packetID == packetType:
        return packet
'''