from tkinter import *
from threading import Thread
from unpacker import *
from lookupData import *

root = Tk()

trackName = StringVar()
sessionType = StringVar()
teamName = StringVar()
driverName = StringVar()
lastLapTime = StringVar()
currentLapTime = StringVar()

checkButtons = [None] * 22
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

def setIntVars(intVarArray, value):
    for intVar in intVarArray:
        intVar.set(value)

def updateData():
    global distance, newSpeed, speed, trackDistance
    packet = RetrievePacket()
    if (packet.packetHeader.packetID == 1):
        track = getTrackData(packet.trackID)
        trackName.set(track["circuit"] + ", " + track["location"] + ", " + track["country"])
        sessionType.set(getSessionType(packet.sessionType, packet.formula))
        trackDistance = packet.trackLength
    if (packet.packetHeader.packetID == 2):
        lastLapTime.set("Previous Lap Time: " + msToString(packet.lapData[packet.packetHeader.playerCarIndex].lastLapTime))
        currentLapTime.set("Current Lap Time: " + msToString(packet.lapData[packet.packetHeader.playerCarIndex].currentLapTime))
        currentLapLabel.config(fg=getValidityTextColour(packet.lapData[packet.packetHeader.playerCarIndex].currentLapInvalid))
        for i in range(22):
            newDistance[i] = packet.lapData[i].lapDistance
            if (showDriverSpeedTrace[i].get() and trackDistance != 0 and newDistance[i] > 0 and newDistance[i] < trackDistance and newDistance > distance):
                speedTrace.create_line(distance[i] / (trackDistance / 1000), 400 - speed[i], newDistance[i] / (trackDistance / 1000), 400 - newSpeed[i], fill = driverColours[i], width = driverWidths[i], tag="trace")
            speed[i] = newSpeed[i]
            distance[i] = newDistance[i]
    if (packet.packetHeader.packetID == 4):
        teamName.set("Team: " + getTeamData(packet.participants[packet.packetHeader.playerCarIndex].teamID)["name"])
        driverName.set("Driver: " + packet.participants[packet.packetHeader.playerCarIndex].name)
        teamIdOccurences = []
        for i in range(22):
            if i < packet.numActiveCars:
                checkButtons[i].grid(column=i%8, row=int(i/8))
            else:
                checkButtons[i].grid_forget()
                showDriverSpeedTrace[i].set(0)
            driverNames[i].set(packet.participants[i].name)
            team = packet.participants[i].teamID
            driverColours[i] = getTeamData(team)["colour"]
            if team not in teamIdOccurences:
                driverWidths[i] = 1
                teamIdOccurences.append(team)
            else:
                driverWidths[i] = 3
    if (packet.packetHeader.packetID == 6):
        for i in range(22):
            newSpeed[i] = packet.carTelemetryData[i].speed
    root.after(1, task)

def task():
    thread = Thread(target = updateData)
    thread.start()

root.title("F1 2021 Telemetry App")
root.geometry("1000x750+100+100")

packFrame = Frame(root)
gridFrame = Frame(root)
packFrame.pack()
gridFrame.pack()

Label(packFrame, textvariable=trackName).pack()
Label(packFrame, textvariable=sessionType).pack()
Label(packFrame, textvariable=teamName).pack()
Label(packFrame, textvariable=driverName).pack()
Label(packFrame, textvariable=lastLapTime).pack()
currentLapLabel = Label(packFrame, textvariable=currentLapTime)
currentLapLabel.pack()

speedTrace = Canvas(packFrame, width=1000, height=400, bg="black")
speedTrace.pack()
speedTrace.create_line(0, 100, 1000, 100, fill="gray")
speedTrace.create_line(0, 200, 1000, 200, fill="gray")
speedTrace.create_line(0, 300, 1000, 300, fill="gray")

Button(text = "Select All", command = lambda: setIntVars(showDriverSpeedTrace, 1)).pack()
Button(text = "Select None", command = lambda: setIntVars(showDriverSpeedTrace, 0)).pack()
Button(text = "Clear Speed Trace", command = lambda: speedTrace.delete("trace")).pack()

for i in range(22):
    checkButtons[i] = Checkbutton(gridFrame, textvariable=driverNames[i], variable=showDriverSpeedTrace[i])

root.after(1, task)
root.mainloop()