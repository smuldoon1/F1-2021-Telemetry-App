from tkinter import *
from threading import Thread
from unpacker import *
from lookupData import *

from telemetryModule import *

import math

root = Tk()

def updateData():
    #packet = RetrievePacket()

    timingBoard.updateSize()
    paceGraph.updateSize()
    pitMonitor.updateSize()
    fuelMonitor.updateSize()
    pitStrategy.updateSize()

    root.geometry("{}x{}".format(round_to_multiple(root.winfo_width(), 5), round_to_multiple(root.winfo_height(), 3)))

    root.after(1, task)

def task():
    thread = Thread(target = updateData)
    thread.start()

def round_to_multiple(x, base):
    return base * round(x / base)

root.title("F1 2021 Telemetry App")
root.geometry("{}x{}".format(1280, 720))

timingBoard = TelemetryModule(root, 0, 0, 2, 2, "red")
paceGraph = TelemetryModule(root, 2, 0, 3, 2, "blue")
pitMonitor = TelemetryModule(root, 0, 2, 1, 1, "yellow")
fuelMonitor = TelemetryModule(root, 1, 2, 1, 1, "green")
pitStrategy = TelemetryModule(root, 2, 2, 3, 1, "brown")

root.after(1, task)
root.mainloop()