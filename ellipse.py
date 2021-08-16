from PyQt5.QtCore import *
class Ellipse:
    def __init__(self):
        self.start = QPoint()
        self.end = QPoint()
    def setStart2(self, s):
        self.start = s
    def setEnd2(self, e):
        self.end = e
    def startPoint2(self):
        return self.start
    def endPoint2(self):
        return self.end
    def paint2(self, painter):
        painter.drawEllipse(self.startPoint2().x(), self.startPoint2().y(), self.endPoint2().x() - self.startPoint2().x(),
                         self.endPoint2().y() - self.startPoint2().y())