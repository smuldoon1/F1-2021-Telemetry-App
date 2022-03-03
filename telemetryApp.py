from tkinter import *
from threading import Thread
from unpacker import *
from lookupData import *

from telemetryModule import *

import math

root = Tk()

root.title("F1 2021 Telemetry App")
root.geometry("{}x{}".format(1200, 800))
root.configure(background="#212026")

telemetry_modules = []

telemetry_data = [None] * 12

def update():
    for telemetry_module in telemetry_modules:
        telemetry_module.frame.after(1, telemetry_module.updateSize)

    root.geometry("{}x{}".format(round_to_multiple(root.winfo_width(), 12), round_to_multiple(root.winfo_height(), 8)))

    root.after(10, update)

def retrieve_packet_task():
    while True:
        packet = retrieve_packet()
        telemetry_data[packet.packetHeader.packetID] = packet

def round_to_multiple(x, base):
    return base * round(x / base)

def create_telemetry_module(name, column, row, x_span, y_span, colour):
    new_module = TelemetryModule(root, name, column, row, x_span, y_span, colour)
    telemetry_modules.append(new_module)

create_telemetry_module("Timing Tower", 0, 0, 3, 6, "gray")
create_telemetry_module("Pace Tower", 3, 0, 2, 6, "gray")
create_telemetry_module("Pace Graph", 5, 0, 7, 3, "gray")
create_telemetry_module("Predicted Finish Graph", 5, 3, 7, 3, "gray")
create_telemetry_module("Pit Monitor", 0, 6, 2, 2, "gray")
create_telemetry_module("Fuel Monitor", 2, 6, 2, 2, "gray")
create_telemetry_module("Weather Forecast", 4, 6, 8, 1, "gray")
create_telemetry_module("Pit Strategy", 4, 7, 8, 1, "gray")

thread = Thread(target = retrieve_packet_task)
thread.start()

root.after(1, update)
root.mainloop()