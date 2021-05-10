from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Rect:

    def __init__(self):
        self.start = QPoint()
        self.end = QPoint()

    def setStart1(self, s):
        self.start = s

    def setEnd1(self, e):
        self.end = e

    def startPoint1(self):
        return self.start

    def endPoint1(self):
        return self.end

    def paint1(self, painter):
        painter.drawRect(self.startPoint1().x(), self.startPoint1().y(), self.endPoint1().x() - self.startPoint1().x(),
                         self.endPoint1().y() - self.startPoint1().y())