#f1 app
from threading import Thread
from unpacker import *
from lookupData import *

#panda 3d
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from math import pi, sin, cos

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # load model
        self.scene = self.loader.loadModel("models/environment")
        # parent model to scene graph (root = render)
        self.scene.reparentTo(self.render)
        # position/scale
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # add the task to taskmanager
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.taskMgr.add(self.updateData, "RunThread")

    # define a procedure to move the camera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    # run thread
    def runThread(self, task):
        thread = Thread(target = self.updateData)
        thread.start()
        return Task.cont

    # get udp packets and update data
    def updateData(self, task):
        global trackLength, speeds
        packet = RetrievePacket()
        if packet == None:
            return
        playerCar = packet.packetHeader.playerCarIndex
        if (packet.packetHeader.packetID == 1):
            dostuff = 1

app = MyApp()
app.run()