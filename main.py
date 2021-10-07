import socket
from struct import *

from packet import *
from motionPacket import *
from sessionPacket import *
from lapPacket import *
from eventPacket import *
from participantsPacket import *
from carSetupsPacket import *

UDP_IP = "0.0.0.0"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

p = 0   # Unpacking index, keeps track of where in the data the next byte should be unpacked from

def UnpackData(data):
    global p
    packetHeader = PacketHeader(unpack("<HBBBBQfIBB", data[p:p+24]))
    p = p + 24
    if packetHeader.packetID == 0:
        packetMotionData = PacketMotionData(packetHeader, data, p)
    elif packetHeader.packetID == 1:
        packetSessionData = PacketSessionData(packetHeader, data, p)
    elif packetHeader.packetID == 2:
        packetLapData = PacketLapData(packetHeader, data, p)
    elif packetHeader.packetID == 3:
        packetEventData = PacketEventData(packetHeader, data, p)
    elif packetHeader.packetID == 4:
        packetParticipantsData = PacketParticipantsData(packetHeader, data, p)
    elif packetHeader.packetID == 5:
        packetCarSetupData = PacketCarSetupData(packetHeader, data, p)

while True:
    p = 0
    data, address = sock.recvfrom(1464)
    UnpackData(data)
