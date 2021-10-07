import socket
from struct import *

from packet import *
from eventPacket import *

UDP_IP = "0.0.0.0"
UDP_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

p = 0   # Unpacking index, keeps track of where in the data the next byte should be unpacked from

def UnpackData(data):
    global p
    packet_header = PacketHeader(unpack("<HBBBBQfIBB", data[p:p+24]))
    p = p + 24
    if packet_header.packetID == 3:
        packet_event_data = PacketEventData(packet_header, data, p)
        print(packet_event_data)

i = 0
while i > -10:
    p = 0
    data, address = sock.recvfrom(1464)
    UnpackData(data)
    i = i + 1
