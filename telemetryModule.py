from tkinter import *

class TelemetryModule():

    frame = None

    def __init__(self, root, column, row, x_span, y_span, colour):
        self.frame = Frame(root, bg = colour)
        self.root = root
        self.x_span = x_span
        self.y_span = y_span

        self.frame.grid(row = row, column = column, columnspan = x_span, rowspan = y_span)

    def updateSize(self):
        self.frame.config(width = int(self.root.winfo_width() / 5) * self.x_span)
        self.frame.config(height = int(self.root.winfo_height() / 3) * self.y_span)
