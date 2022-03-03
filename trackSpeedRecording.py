from tkinter import *
from threading import Thread
from unpacker import *
from lookupData import *

from math import floor
from operator import itemgetter

root = Tk()

divisions = 10

distance = 0
speed = 0

speedTrace = []

def updateData():
    global distance, speed, speedTrace
    packet = retrieve_packet()
    if packet == None:
        return
    playerCar = packet.packetHeader.playerCarIndex
    if (packet.packetHeader.packetID == 1):
        trackLength = packet.trackLength
        if (len(speedTrace) == 0):
            speedTrace = [0] * int(trackLength / divisions)
    if (packet.packetHeader.packetID == 2):
        distance = packet.lapData[playerCar].lapDistance
        if (len(speedTrace) > 0 and packet.lapData[playerCar].currentLapNum == 1):
            speedTrace[int(distance / divisions) - 1] = speed
    if (packet.packetHeader.packetID == 6):
        speed = packet.carTelemetryData[playerCar].speed
    print(speedTrace)
    root.after(1, task)

def task():
    thread = Thread(target = updateData)
    thread.start()

root.title("F1 2021 Telemetry App")
root.geometry("1000x750+100+100")

canvas = Canvas(root)
canvas.pack()

root.after(1, task)
root.mainloop()