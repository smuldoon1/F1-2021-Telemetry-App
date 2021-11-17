from tkinter import *
import threading
from unpacker import *

root = Tk()

driverName = StringVar()
lastLapTime = StringVar()
currentLapTime = StringVar()

positionX = 0
positionZ = 0

def msToString(ms):
    milliseconds = (ms % 1000)
    seconds = (ms / 1000) % 60
    minutes = (ms / (1000 * 60)) % 60
    hours = (ms / (1000 * 60 * 60)) % 24

    return "{:02d}".format(int(hours)) + ":" + "{:02d}".format(int(minutes)) + ":" + "{:02d}".format(int(seconds)) + "." + "{:03d}".format(int(milliseconds))

def getValidityTextColour(boolean):
    if boolean == 0:
        return "#000"
    return "#f00"

def task():
    #canvas.delete("all")
    packet = RetrievePacket()
    if (packet.packetHeader.packetID == 0):
        positionX = 200 + packet.carMotionData[packet.packetHeader.playerCarIndex].worldPositionX / 5
        positionZ = 200 + packet.carMotionData[packet.packetHeader.playerCarIndex].worldPositionZ / 5
        canvas.create_oval(positionX, positionZ, positionX + 10, positionZ + 10, fill = "white", outline = "white")
        driverName.set("Pos: " + str(packet.carMotionData[packet.packetHeader.playerCarIndex].worldPositionX) + ", " + str(packet.carMotionData[packet.packetHeader.playerCarIndex].worldPositionY))
    if (packet.packetHeader.packetID == 2):
        lastLapTime.set("Previous Lap Time: " + msToString(packet.lapData[packet.packetHeader.playerCarIndex].lastLapTime))
        currentLapTime.set("Current Lap Time: " + msToString(packet.lapData[packet.packetHeader.playerCarIndex].currentLapTime))
        currentLapLabel.config(fg=getValidityTextColour(packet.lapData[packet.packetHeader.playerCarIndex].currentLapInvalid))
    if (packet.packetHeader.packetID == 4):
        #driverName.set("Driver: " + packet.participants[packet.packetHeader.playerCarIndex].name)
        a = 1
    root.after(1, task)

root.title("F1 2021 Telemetry App")
root.geometry("400x500+100+100")

Label(root, textvariable=driverName).pack()
Label(root, textvariable=lastLapTime).pack()
currentLapLabel = Label(root, textvariable=currentLapTime)
currentLapLabel.pack()

canvas = Canvas(root, width=400, height=400, bg="black")
canvas.pack()

root.after(1, task)
root.mainloop()