from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from rect import Rect
from ellipse import Ellipse


class My_Board(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(598, 498)  # 考虑边框的间距 减去px

        self._IfEmpty = 1
        self.Draw = "画线"
        self.pixmap.fill(Qt.white)
        self.setStyleSheet("border: 1px solid black")
        self.Color = Qt.black  # pen color: black
        self.penwidth = 1  # pen width : 1
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.start = QPoint()
        self.stop = QPoint()
        self.situation1 = False  # 描述在不在画
        self.shape1 = None  # 存储画过的矩形
        self.rect_list = []  # 将画过的矩形存到此数组中
        self.situation2 = False  # 描述在不在画
        self.shape2 = None  # 存储画过的椭圆
        self.ellipse_list = [] # 将画过的矩形存到此数组中
        self.pos_xy = [] #
        self.points = []  # 储存读取的坐标点
        self.drawpath = False
        self.coord_rect_all = []
        self.coord_elli_all = []
        self.elli_long_all =[]
        self.elli_short_all = []
        self.initui()
        # 显示坐标

    def initui(self):

        self.setMouseTracking(False)
        self.setGeometry(500, 300, 100, 25)
        self.setWindowTitle('Event object')
        self.show()

    def make_image(self):
        #获取画板内容（返回QImage）
        img = self.pixmap.toImage()
        return img


    def paintEvent(self, event):

        self.painter = QPainter(self)  # 建立绘图工具
        size = self.size()  # 获得窗口的尺寸。

        self.painter.begin(self.pixmap)
        # self.painter.setRenderHint(Antialiasing,True)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.setPen(QPen(self.Color, self.penwidth, Qt.SolidLine))

        if self.points:
            self.painter.drawPolygon(QPolygon(self.points))

        if self._IfEmpty == 0:
            self.ellipse_list = []
            self.rect_list = []
            self._IfEmpty = 1
        else:
            for self.shape2 in self.ellipse_list:
                self.shape2.paint2(self.painter)
            for self.shape1 in self.rect_list:
                self.shape1.paint1(self.painter)

        self.painter.end()

    def mousePressEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()

        if event.button() == Qt.LeftButton:

            if self.Draw == "画线":

                self.endPoint = event.pos()
                self.lastPoint = self.endPoint
                self.update()

            elif self.Draw == "椭圆":
                self.shape2 = Ellipse()
                if self.shape2 is not None:
                    self.situation2 = False
                    self.ellipse_list.append(self.shape2)
                    self.shape2.setStart2(event.pos())
                    self.shape2.setEnd2(event.pos())
                # self.update()
            elif self.Draw == "矩形":
                self.shape1 = Rect()
                if self.shape1 is not None:
                    self.situation1 = False
                    self.rect_list.append(self.shape1)
                    self.shape1.setStart1(event.pos())
                    self.shape1.setEnd1(event.pos())

                self.update()

        # self.__IsEmpty = False

    # 显示坐标
    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        window = self.parent().window()
        if window is not None:
            self.parent().window().Board_Coordinates.setText('X: %d; Y: %d' % (event.x(), event.y()))

        # text = "x:{0},y:{1}".format(x, y)
        # self.label.setText(text)
        self.painter.begin(self.pixmap)
        self.painter.setPen(QPen(self.Color, self.penwidth, Qt.SolidLine))
            # self.painter.setPen(QColor(self.Color))

        if self.Draw == "画线":
            self.endPoint = event.pos()
            self.painter.drawLine(self.lastPoint, self.endPoint)
            self.lastPoint = self.endPoint
            self.update()

        elif self.Draw == "椭圆":
            if self.shape2 is not None and not self.situation2:
                self.shape2.setEnd2(event.pos())
                self.update()

        elif self.Draw == "矩形":
            if self.shape1 is not None and not self.situation1:
                self.shape1.setEnd1(event.pos())
                self.update()

        self.painter.end()

    def mouseReleaseEvent(self, event):
        self.x2 = event.x()
        self.y2 = event.y()
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            if self.Draw == '矩形':
                self.situation1 = True
                self.shape1 = None
                coord_rect = [[self.x1, self.y1], [self.x2, self.y1], [self.x1, self.y2], [self.x2, self.y2]]
                self.coord_rect_all.append(coord_rect)
                print(self.coord_rect_all)
            if self.Draw == '椭圆':
                self.situation2 = True
                self.shape2 = None
                coord_elli = [(self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2]
                elli_long = [self.x2, (self.y1 + self.y2) / 2]
                elli_short = abs((self.y1 - self.y2) / 2)
                self.coord_elli_all.append(coord_elli)
                self.elli_long_all.append(elli_long)
                self.elli_short_all.append(elli_short)
                print(self.coord_elli_all)
            self.update()
