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

speeds = [0] * 22

bahrainSpeeds = [294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 304, 305, 306, 306, 307, 308, 308, 309, 309, 310, 310, 311, 311, 312, 312, 313, 313, 313, 314, 314, 315, 315, 315, 315, 316, 316, 316, 316, 317, 317, 317, 317, 317, 318, 318, 318, 318, 318, 318, 318, 319, 319, 319, 319, 319, 319, 319, 319, 320, 319, 303, 287, 261, 243, 218, 187, 158, 137, 114, 90, 79, 76, 75, 72, 79, 87, 92, 93, 100, 111, 122, 133, 135, 147, 160, 169, 177, 181, 186, 192, 198, 200, 204, 207, 213, 218, 223, 225, 230, 234, 238, 242, 245, 248, 252, 254, 257, 259, 262, 264, 266, 270, 272, 273, 275, 278, 279, 281, 283, 284, 286, 287, 288, 289, 290, 291, 293, 294, 295, 296, 297, 297, 298, 300, 300, 301, 302, 303, 303, 304, 304, 289, 262, 247, 220, 189, 167, 149, 134, 129, 126, 123, 121, 118, 115, 114, 120, 128, 137, 144, 154, 165, 175, 184, 190, 197, 201, 209, 214, 219, 224, 229, 233, 237, 241, 243, 247, 250, 252, 253, 256, 258, 260, 238, 216, 194, 182, 173, 169, 167, 168, 171, 178, 184, 191, 200, 206, 211, 215, 215, 216, 217, 220, 222, 223, 231, 235, 239, 241, 244, 247, 250, 252, 255, 258, 261, 254, 229, 197, 178, 144, 126, 123, 117, 106, 96, 90, 86, 82, 86, 98, 113, 130, 141, 155, 167, 177, 185, 192, 198, 206, 212, 217, 222, 225, 229, 234, 236, 239, 242, 245, 248, 252, 255, 257, 260, 262, 264, 265, 268, 269, 270, 260, 244, 222, 197, 173, 149, 127, 114, 92, 87, 84, 83, 82, 90, 99, 114, 129, 140, 153, 165, 174, 183, 191, 200, 206, 212, 218, 223, 228, 233, 237, 239, 245, 249, 251, 254, 257, 259, 261, 261, 262, 270, 272, 274, 276, 279, 280, 282, 284, 285, 287, 287, 289, 290, 291, 292, 293, 295, 296, 297, 298, 299, 300, 301, 302, 302, 303, 304, 305, 305, 306, 307, 307, 297, 280, 262, 236, 214, 196, 184, 175, 171, 168, 166, 163, 161, 158, 163, 168, 173, 180, 185, 191, 194, 199, 202, 206, 210, 216, 220, 223, 228, 232, 236, 238, 241, 245, 248, 251, 252, 255, 257, 259, 261, 262, 264, 265, 266, 267, 267, 265, 265, 266, 267, 268, 269, 269, 270, 271, 271, 272, 273, 274, 275, 276, 278, 279, 280, 281, 282, 270, 235, 218, 202, 184, 166, 161, 143, 140, 142, 144, 153, 154, 167, 170, 179, 186, 193, 198, 204, 211, 217, 221, 225, 230, 231, 235, 239, 244, 248, 250, 252, 255, 258, 260, 262, 265, 266, 268, 270, 272, 273, 275, 277, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 289, 291, 291, 292, 293, 293, 294, 295, 295, 296, 296, 297, 297, 297, 298, 299, 299, 299, 300, 300, 300, 300, 301, 301, 301, 284, 276, 240, 213, 187, 162, 151, 131, 127, 125, 125, 135, 142, 147, 147, 146, 149, 155, 154, 160, 169, 174, 183, 191, 199, 206, 211, 215, 222, 226, 230, 235, 237, 241, 245, 248, 251, 254, 256, 259, 261, 263, 264, 268, 271, 273, 276, 277, 279, 280, 281, 284, 285, 287, 288, 289, 290]

sessionTime = StringVar()
lapDistance = StringVar()
percentage = StringVar()

nearbyDrivers = StringVar()

def trackDistance(value, trackLength):
    if value < 0:
        return trackLength + value
    return value

def getTimeDelta(dist1, dist2):
    i1 = int(dist1 / 10)
    i2 = int(dist2 / 10)
    totalSpeed = 0
    totalDistance = 0
    for i in range(i1, i2):
        if (i >= len(bahrainSpeeds)):
            i = 0
        totalSpeed += bahrainSpeeds[i]
        totalDistance += 10
    return totalSpeed * 0.277778 / (totalDistance + 0.001)

def updateData():
    global trackLength, speeds
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
                nearby += str(int(dist)) + "m : "
                timeDelta = getTimeDelta(packet.lapData[playerCar].lapDistance, packet.lapData[sortedLapDistances[(spi + i) % len(sortedLapDistances)][0]].lapDistance)
                nearby += '{0:.3f}'.format(timeDelta) + "s\n"
        nearbyDrivers.set(nearby)

        # Own car data
        ld = packet.lapData[playerCar].lapDistance
        td = trackDistance(ld, trackLength)
        lapDistance.set(str(int(td)) + "/" + str(trackLength) + "m")
        percentage.set(str(int(td / trackLength * 100)) + "%")
    if (packet.packetHeader.packetID == 4):
        for i in range(22):
            names[i] = packet.participants[i].name
    if (packet.packetHeader.packetID == 6):
        for i in range(22):
            speeds[i] = packet.carTelemetryData[i].speed
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