from tkinter import *

class TelemetryModule():
    def __init__(self, root, name, column, row, x_span, y_span, colour):
        self.root = root
        self.name = name
        self.x_span = x_span
        self.y_span = y_span

        self.frame = Frame(root, bg = colour)
        self.header = Label(self.frame, text = name)
        self.frame.grid(row = row, column = column, columnspan = x_span, rowspan = y_span, padx = 5, pady = 5)
        self.header.grid()

    def updateSize(self):
        self.frame.config(width = int(self.root.winfo_width() / 12) * self.x_span - 10)
        self.frame.config(height = int(self.root.winfo_height() / 8) * self.y_span - 10)
