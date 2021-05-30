import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from rect import Rect
from ellipse import Ellipse
# from Physical_boundary_acquisition import *
# from looking_for_vertices import *
from tkinter import filedialog

# from functions import rank
# from polygon import *
# from round import *
import json
import os
import copy
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.ellipse_list = []
        self.erasemode = False  # 默认不开启橡皮擦
        self.pos_xy = []
        self.points = []  # 储存读取的坐标点
        self.drawpath = False
        self.initui()
        # 显示坐标

    def initui(self):
        # grid = QGridLayout()
        # grid.setSpacing(100)
        # self.setLayout(grid)

        x = 0
        y = 0

        self.text = "x:{0},Y:{0}".format(x, y)
        # self.label = QLabel(self.text, self)
        # grid.addWidget(self.label, 20, 20, Qt.AlignTop)
        self.setMouseTracking(False)
        # self.setLayout(grid)
        self.setGeometry(500, 300, 100, 25)
        self.setWindowTitle('Event object')
        self.show()

    def GetContentAsQImage(self):
        #获取画板内容（返回QImage）
        img = self.pixmap.toImage()
        return img


    def paintEvent(self, event):

        self.painter = QPainter(self)  # 建立绘图工具

        size = self.size()  # 获得窗口的尺寸。

        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.setPen(QPen(self.Color, self.penwidth, Qt.SolidLine))

        if self.points:
            self.painter.drawPolygon(QPolygon(self.points))

        if self.Draw == "圆形":

            if self._IfEmpty == 0:
                self.ellipse_list = []
                self._IfEmpty = 1
            else:
                for self.shape2 in self.ellipse_list:
                    self.shape2.paint2(self.painter)

        elif self.Draw == "矩形":
            if self._IfEmpty == 0:
                self.rect_list = []
                self._IfEmpty = 1
            else:
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

            elif self.Draw == "圆形":
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
        if self.erasemode == False:
            self.painter.setPen(QPen(self.Color, self.penwidth, Qt.SolidLine))
            # self.painter.setPen(QColor(self.Color))
        else:
            self.painter.setPen(QPen(Qt.white, 4, Qt.SolidLine))

        if self.Draw == "画线":
            self.endPoint = event.pos()
            self.painter.drawLine(self.lastPoint, self.endPoint)
            self.lastPoint = self.endPoint
            self.update()

        elif self.Draw == "圆形":
            if self.shape2 is not None and not self.situation2:
                self.shape2.setEnd2(event.pos())
                self.update()

        elif self.Draw == "矩形":
            if self.shape1 is not None and not self.situation1:
                self.shape1.setEnd1(event.pos())
                self.update()

        self.painter.end()
        # 中间变量pos_tmp提取当前点
        # pos_tmp = (event.pos().x(), event.pos().y())
        #
        # # 将坐标值打印到小黑框里
        # print(pos_tmp)

        # 将坐标值导出
        # data = open(r"D:\pycharm\git-bfc2021\画板坐标.txt", 'a')
        # data.write(str(pos_tmp))
        # data.write("\t")
        # data.close()
        # pos_tmp添加到self.pos_xy中
        # self.pos_xy.append(pos_tmp)

    def mouseReleaseEvent(self, event):
        self.x2 = event.x()
        self.y2 = event.y()
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            if self.Draw == '矩形':
                self.situation1 = True
                self.shape1 = None
                self.coord_rect = [[self.x1, self.y1], [self.x2, self.y1], [self.x1, self.y2], [self.x2, self.y2]]
                print(self.coord_rect)
            if self.Draw == '圆形':
                self.situation2 = True
                self.shape2 = None
                self.coord_elli = [(self.x1 + self.x2)/2, (self.y1 + self.y2)/2]
                self.elli_long = abs((self.x1 - self.x2)/2)
                self.elli_short = abs((self.y1 - self.y2)/2)
                print(self.coord_elli)
            self.update()

        # self.__IsEmpty = False