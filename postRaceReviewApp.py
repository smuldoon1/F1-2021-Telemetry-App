#f1 app
from threading import Thread
from unpacker import *
from lookupData import *

#panda 3d
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *

from math import pi

class MyApp(ShowBase):
    global hasSetCam
    def __init__(self):
        ShowBase.__init__(self)

        #self.floor = self.loader.load_model("floor.obj")

        self.cars = [None] * 22
        for i in range(22):
            self.cars[i] = self.loader.load_model("car.bam")
            self.cars[i].reparentTo(self.render)
            self.cars[i].setScale(0.75, 0.75, 0.75)
        #self.camera.reparentTo(self.car)

        # add the task to taskmanager
        self.taskMgr.add(self.updateData, "UpdateData")

    # get udp packets and update data
    def updateData(self, task):
        packet = retrieve_packet()
        #if packet == None:
        #    return
        playerCar = packet.packetHeader.playerCarIndex
        self.camera.reparentTo(self.cars[playerCar])
        self.camera.setPos(0, 12, 4)
        self.camera.setHpr(180, 345, 0)
        base.camLens.setFov(45)
        if (packet.packetHeader.packetID == 0):
            for i in range(22):
                cmd = packet.carMotionData[i]
                if i == playerCar:
                    print("X: " + str(int(cmd.worldPositionX)) + "\tZ: " + str(int(cmd.worldPositionZ)) + "\tY: " + str(int(cmd.worldPositionY)))
                    print("H: " + str(int(cmd.yaw * 180.0 / pi)) + "\tP: " + str(int(cmd.pitch * 180.0 / pi)) + "\tR: " + str(int(cmd.roll * 180.0 / pi)))
                self.cars[i].setPos(-cmd.worldPositionX, cmd.worldPositionZ, cmd.worldPositionY)
                self.cars[i].setHpr(self.render, 180 - cmd.yaw * -180.0 / pi, cmd.pitch * 180.0 / pi, -cmd.roll * 180.0 / pi)
        if (packet.packetHeader.packetID == 4):
            for i in range(22):
                r, g, b = hexToRgb(getTeamData(packet.participants[i].teamID)["colour"])
                self.cars[i].setColor(r / 255.0, g / 255.0, b / 255.0, 1.0)
        return Task.cont

app = MyApp()
app.run()