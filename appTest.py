from tkinter import *
import threading
from unpacker import *

root = Tk()

driverName = StringVar()
lastLapTime = StringVar()
currentLapTime = StringVar()

showDriverSpeedTrace = [None] * 22
driverNames = [None] * 22

for i in range(22):
    showDriverSpeedTrace[i] = IntVar()
    driverNames[i] = StringVar()

newSpeed = [0] * 22
speed = [0] * 22
newDistance = [0] * 22
distance = [0] * 22
trackDistance = 0

driverColours = ["#000"] * 22
driverWidths = [1] * 22

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

def getTeamColour(teamId):
    if teamId == 0: # Mercedes
        return "#00D2BE"
    if teamId == 1: # Ferrari
        return "#DC0000"
    if teamId == 2: # Red bull
        return "#0600EF"
    if teamId == 3: # Williams
        return "#005AFF"
    if teamId == 4: # Aston martin
        return "#006F62"
    if teamId == 5: # Alpine
        return "#0090FF"
    if teamId == 6: # Alpha tauri
        return "#2B4562"
    if teamId == 7: # Haas
        return "#FFFFFF"
    if teamId == 8: # Mclaren
        return "#FF8700"
    if teamId == 9: # Alfa
        return "#900000"
    return "#ffffff"

def task():
    global distance, newSpeed, speed, trackDistance
    packet = RetrievePacket()
    if (packet.packetHeader.packetID == 1):
        trackDistance = packet.trackLength
    if (packet.packetHeader.packetID == 2):
        lastLapTime.set("Previous Lap Time: " + msToString(packet.lapData[packet.packetHeader.playerCarIndex].lastLapTime))
        currentLapTime.set("Current Lap Time: " + msToString(packet.lapData[packet.packetHeader.playerCarIndex].currentLapTime))
        currentLapLabel.config(fg=getValidityTextColour(packet.lapData[packet.packetHeader.playerCarIndex].currentLapInvalid))
        for i in range(22):
            newDistance[i] = packet.lapData[i].lapDistance
            if (showDriverSpeedTrace[i].get() and trackDistance != 0 and newDistance[i] > 0 and newDistance[i] < trackDistance and newDistance > distance):
                speedTrace.create_line(distance[i] / (trackDistance / 1000), 400 - speed[i], newDistance[i] / (trackDistance / 1000), 400 - newSpeed[i], fill = driverColours[i], width = driverWidths[i])
            speed[i] = newSpeed[i]
            distance[i] = newDistance[i]
    if (packet.packetHeader.packetID == 4):
        driverName.set("Driver: " + packet.participants[packet.packetHeader.playerCarIndex].name)
        teamIdOccurences = []
        for i in range(22):
            driverNames[i].set(packet.participants[i].name)
            team = packet.participants[i].teamID
            driverColours[i] = getTeamColour(team)
            if team not in teamIdOccurences:
                driverWidths[i] = 1
                teamIdOccurences.append(team)
            else:
                driverWidths[i] = 3
    if (packet.packetHeader.packetID == 6):
        for i in range(22):
            newSpeed[i] = packet.carTelemetryData[i].speed
    root.after(1, task)

root.title("F1 2021 Telemetry App")
root.geometry("1000x600+100+100")

packFrame = Frame(root)
gridFrame = Frame(root)
packFrame.pack()
gridFrame.pack()

Label(packFrame, textvariable=driverName).pack()
Label(packFrame, textvariable=lastLapTime).pack()
currentLapLabel = Label(packFrame, textvariable=currentLapTime)
currentLapLabel.pack()

speedTrace = Canvas(packFrame, width=1000, height=400, bg="black")
speedTrace.pack()

for i in range(22):
    Checkbutton(gridFrame, textvariable=driverNames[i], variable=showDriverSpeedTrace[i]).grid(column=i%8, row=int(i/8))

root.after(1, task)
root.mainloop()