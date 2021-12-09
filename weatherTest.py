from tkinter import *
from threading import Thread
from unpacker import *
from lookupData import *

root = Tk()

weatherSamples = StringVar()

def getWeatherString(weatherIndex):
    if weatherIndex == 0:
        return "Clear"
    if weatherIndex == 1:
        return "Light Clouds"
    if weatherIndex == 2:
        return "Overcast"
    if weatherIndex == 3:
        return "Light Rain"
    if weatherIndex == 4:
        return "Heavy Rain"
    if weatherIndex == 5:
        return "Torrential Rain"

def updateData():
    global distance, newSpeed, speed, trackDistance
    packet = RetrievePacket()
    if (packet.packetHeader.packetID == 1):
        weather = ""
        for i in range(packet.numWeatherForecastSamples):
            wfs = packet.weatherForecastSamples[i]
            weather += str(wfs.timeOffset) + " - " + getWeatherString(wfs.weather) + " : " + str(wfs.rainPercentage) + "%\n"
        weatherSamples.set(weather)
    root.after(1, task)

def task():
    thread = Thread(target = updateData)
    thread.start()

root.title("F1 2021 Telemetry App")
root.geometry("1000x750+100+100")

Label(root, textvariable=weatherSamples).pack()

root.after(1, task)
root.mainloop()