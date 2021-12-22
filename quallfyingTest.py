from tkinter import *
from threading import Thread
from unpacker import *
from lookupData import *

from math import floor
from operator import itemgetter

root = Tk()

trackLength = 1
lapDistances = [None] * 22
names = [""] * 22

sessionTime = StringVar()
lapDistance = StringVar()
percentage = StringVar()

nearbyDrivers = StringVar()

def trackDistance(value, trackLength):
    if value < 0:
        return trackLength + value
    return value

def updateData():
    global trackLength
    packet = RetrievePacket()
    playerCar = packet.packetHeader.playerCarIndex
    if (packet.packetHeader.packetID == 1):
        sessionTime.set(str(floor(packet.sessionTimeLeft / 60)) + ":" + str(floor(packet.sessionTimeLeft % 60)) + "/" + str(floor(packet.sessionDuration / 60)) + ":" + str(floor(packet.sessionDuration % 60)))
        trackLength = packet.trackLength
    if (packet.packetHeader.packetID == 2):
        lapDistances = []
        for i in range(22):
            if packet.lapData[i].driverStatus != 0:
                lapDistances.append([i, trackDistance(packet.lapData[playerCar].lapDistance, trackLength) - trackDistance(packet.lapData[i].lapDistance, trackLength)])
        sortedLapDistances = sorted(lapDistances, key=itemgetter(1))
        spi = -1
        for i in range(len(sortedLapDistances)):
            if sortedLapDistances[i][0] == playerCar:
                spi = i
        nearby = str(spi) + "\n"
        for i in range(-3, 4):
            if packet.lapData[sortedLapDistances[(spi + i) % len(sortedLapDistances)][0]].driverStatus != 0:
                nearby += names[sortedLapDistances[(spi + i) % len(sortedLapDistances)][0]] + " : "
                dist = sortedLapDistances[(spi + i) % len(sortedLapDistances)][1]
                if i < 0 and dist > 0:
                    dist -= trackLength
                elif i > 0 and dist < 0:
                    dist += trackLength
                nearby += str(int(dist)) + "m\n"
        nearbyDrivers.set(nearby)

        # Own car data
        ld = packet.lapData[playerCar].lapDistance
        td = trackDistance(ld, trackLength)
        lapDistance.set(str(int(td)) + "/" + str(trackLength) + "m")
        percentage.set(str(int(td / trackLength * 100)) + "%")
    if (packet.packetHeader.packetID == 4):
        for i in range(22):
            names[i] = packet.participants[i].name
    root.after(1, task)

def task():
    thread = Thread(target = updateData)
    thread.start()

root.title("F1 2021 Telemetry App")
root.geometry("1000x750+100+100")

Label(root, textvariable=sessionTime).pack()
Label(root, textvariable=lapDistance).pack()
Label(root, textvariable=percentage).pack()
Label(root, textvariable=nearbyDrivers).pack()

root.after(1, task)
root.mainloop()