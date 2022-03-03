from unpacker import *
import math
import matplotlib.pyplot as plt

speed = 0
driverIndex = -1

laps = [1,2,3,4,5]

while True:
    packet = retrieve_packet()
    driverIndex = packet.packetHeader.playerCarIndex
    if packet.packetHeader.packetID == 11:
        if packet.carIdx == driverIndex:
            lapTimes = []
            for i in range(len(laps)):#len(packet.lapHistoryData)):
                lapTimes.append(packet.lapHistoryData[i].lapTime)
            plt.plot(laps, lapTimes[0:len(laps)])
            plt.show()
            