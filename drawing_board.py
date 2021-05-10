import sys
import cv2
import tkinter as tk
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from rect import Rect
from ellipse import Ellipse
from Physical_boundary_acquisition import *
from looking_for_vertices import *
from tkinter import filedialog

from functions import rank
from polygon import *
from round import *
import json
import os
import copy
from PyQt5 import QtCore, QtGui, QtWidgets


class My_Board(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(598, 498)  # 考虑边框的间距 减去px

        self.__IsEmpty = True
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

    def IsEmpty(self):
        # 返回画板是否为空
        return self.__IsEmpty

    def paintEvent(self, event):

        self.painter = QPainter(self)  # 建立绘图工具

        size = self.size()  # 获得窗口的尺寸。

        self.painter.begin(self)
        self.painter.drawPixmap(0, 0, self.pixmap)

        if self.points:
            self.painter.drawPolygon(QPolygon(self.points))

        if self.Draw == "圆形":
            for self.shape2 in self.ellipse_list:
                self.shape2.paint2(self.painter)

        elif self.Draw == "矩形":
            if self.__IsEmpty == True:
                self.pixmap.fill(Qt.white)
            else:
                for self.shape1 in self.rect_list:
                    self.shape1.paint1(self.painter)

        self.painter.end()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            if self.Draw == "画线":

                self.endPoint = event.pos()
                self.lastPoint = self.endPoint
                self.update()

            elif self.Draw == "圆形":
                self.shape2 = Ellipse()
                if (self.shape2 is not None):
                    self.situation2 = False
                    self.ellipse_list.append(self.shape2)
                    self.shape2.setStart2(event.pos())
                    self.shape2.setEnd2(event.pos())
                # self.update()
            elif self.Draw == "矩形":
                self.shape1 = Rect()
                if (self.shape1 is not None):
                    self.situation1 = False
                    self.rect_list.append(self.shape1)
                    self.shape1.setStart1(event.pos())
                    self.shape1.setEnd1(event.pos())

                self.update()

        self.__IsEmpty = False

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
        pos_tmp = (event.pos().x(), event.pos().y())

        # 将坐标值打印到小黑框里
        print(pos_tmp)

        # 将坐标值导出
        # data = open(r"D:\pycharm\git-bfc2021\画板坐标.txt", 'a')
        # data.write(str(pos_tmp))
        # data.write("\t")
        # data.close()
        # pos_tmp添加到self.pos_xy中
        self.pos_xy.append(pos_tmp)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            if self.Draw == '矩形':
                self.situation1 = True
                self.shape1 = None
            if self.Draw == '圆形':
                self.situation2 = True
                self.shape2 = None
            self.update()

        self.__IsEmpty = False


class window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('grid generation software')
        self.initUi()
        self.h = 0
        self.w = 0

    def initUi(self):
        self.resize(750, 550)

        # 新建一个水平布局作为本窗体的主布局
        main_layout = QHBoxLayout(self)
        # 设置主布局内边距以及控件间距为10px
        main_layout.setSpacing(10)

        vbox = QVBoxLayout()
        # 选择绘画文件 按钮
        self.button_file = QPushButton("文件")
        self.button_file.setParent(self)
        self.button_file.setGeometry(20, 80, 75, 25)
        self.button_file.setFont(QFont("Chiller", 10))
        vbox.addWidget(self.button_file)
        vbox.addStretch()
        # 选择画笔颜色 按钮
        self.button_color = QPushButton(self)
        self.button_color.setGeometry(20, 120, 75, 25)
        self.button_color.setText("画笔颜色")
        self.button_color.setFont(QFont("Chiller", 10))
        vbox.addWidget(self.button_color)
        vbox.addStretch()
        # 选择画笔粗细 按钮
        self.button_width = QPushButton(self)
        self.button_width.setGeometry(20, 160, 75, 25)
        self.button_width.setText("画笔粗细")
        self.button_width.setFont(QFont("Chiller", 10))
        vbox.addWidget(self.button_width)
        vbox.addStretch()
        # 清空画板 按钮
        self.button_Clear = QPushButton(self)
        self.button_Clear.setGeometry(20, 200, 75, 25)
        self.button_Clear.setText("清空")
        self.button_Clear.setFont(QFont("Chiller", 10))
        vbox.addWidget(self.button_Clear)
        vbox.addStretch()
        # 使用橡皮擦
        self.button_Eraser = QCheckBox(self)
        self.button_Eraser.setParent(self)
        self.button_Eraser.setGeometry(20, 240, 75, 25)
        self.button_Eraser.setText(" 橡皮擦")
        self.button_Clear.setFont(QFont("Chiller", 10))
        vbox.addWidget(self.button_Eraser)
        vbox.addStretch()

        # 选择画不同的图形
        self.graphoto1 = QComboBox(self)
        information = ['画线', '矩形', '圆形']
        self.graphoto1.addItems(information)
        self.graphoto1.setGeometry(20, 280, 75, 25)
        self.graphoto1.currentIndexChanged.connect(self.choose_graph)

        # 设置画板
        self.My_Paper = My_Board(self)
        self.My_Paper.setGeometry(120, 10, 601, 501)

        self.button_file.clicked.connect(self.openfile)
        self.button_color.clicked.connect(self.choose_color)
        self.button_width.clicked.connect(self.choose_width)
        self.button_Clear.clicked.connect(self.paint_BoardClear)
        self.button_Eraser.clicked.connect(self.Eraser)

        self.statusBar().showMessage('                              坐标')
        self.statusBar().show()
        self.Board_Coordinates = QLabel('')
        self.statusBar().addPermanentWidget(self.Board_Coordinates)

    def openfile(self):
        # fpath = QFileDialog.getOpenFileName(self, "选择文件", ".")
        # Realpath = os.path.split(fpath[-2])[:-1]
        # os.chdir(Realpath[0]) # 修改读取图片的路径
        # fname = os.path.split(fpath[-2])[-1]
        # img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

        root = tk.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename()  # 获得选好的文件
        img = cv_imread(Filepath)

        img1 = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)  # 将图片显示为原来的60%
        # cv2.namedWindow(img,cv2.WINDOW_NORMAL)
        cv2.imshow('IMREAD_GRAYSCALE+Color', img1)
        self.h, self.w = img.shape[:]
        # self.h, self.w = 700,500

        self.num_edges = 1  # 多边形的边数
        cv2.waitKey(0)
        self.box = QMessageBox(QMessageBox.Question, '选择', '选择图形', QMessageBox.NoButton, self)
        self.choice1 = self.box.addButton('正放矩形', QMessageBox.YesRole)
        self.choice2 = self.box.addButton('正放椭圆形', QMessageBox.YesRole)
        self.choice3 = self.box.addButton('多边形', QMessageBox.YesRole)
        self.choice4 = self.box.addButton('斜放矩形', QMessageBox.YesRole)
        self.box.show()

        self.choice1.clicked.connect(lambda: self.bt_choice1(img))
        self.choice2.clicked.connect(lambda: self.bt_choice2(img))
        self.choice3.clicked.connect(lambda: self.bt_choice3(img))
        self.choice4.clicked.connect(lambda: self.bt_choice4(img))

        # QMessageBox.question(self, '选择', '选择图形', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # cv2.destroyAllWindows()

        # fname = os.path.split(fpath[-2])[-1]
        # with open(fname) as ex:
        #     a=json.load(ex)
        # filename = copy.deepcopy(a)
        # # filename = rank(filename)
        # print(filename)
        # self.spots = []
        # for i in range(len(filename)):
        #     a = QPoint(filename[i][0],filename[i][1])
        #     self.spots.append(a)
        # self.lb.points = copy.deepcopy(self.spots)

    def bt_choice1(self, image):
        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_rectangular_1(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        boundary_coordinates1 = change_coordinate(self.h, boundary_coordinates)
        plots = np.array(boundary_coordinates1)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def bt_choice2(self, image):
        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_circle(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        boundary_coordinates1 = change_coordinate(self.h, boundary_coordinates)
        plots = np.array(boundary_coordinates1)
        a = circular(plots,50,50)
        center,r2 = a.feature()
        # print(center[0])
        a.mesh(5)

    def bt_choice3(self, image):
        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_polygon(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        boundary_coordinates1 = change_coordinate(self.h, boundary_coordinates)
        plots = np.array(boundary_coordinates1)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def bt_choice4(self, image):
        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_rectangular_2(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        # print(boundary_coordinates)
        boundary_coordinates1 = change_coordinate(self.h, boundary_coordinates)
        # print(boundary_coordinates1)
        plots = np.array(boundary_coordinates1)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def choose_color(self):
        Color = QColorDialog.getColor()  # color是Qcolor
        if Color.isValid():
            self.My_Paper.Color = Color

    # 设置橡皮擦模式
    def Eraser(self):
        if self.button_Eraser.isChecked():
            self.My_Paper.erasemode = True
        else:
            self.My_Paper.erasemode = False

    # 选择画笔粗细
    def choose_width(self):
        width, ok = QInputDialog.getInt(self, '选择画笔粗细', '请输入粗细：', min=1, step=1)
        if ok:
            self.My_Paper.penwidth = width

    # 清空画板
    def paint_BoardClear(self):
        self.My_Paper.__IsEmpty = True
        self.My_Paper.pixmap.fill(Qt.white)
        self.update()

    # 选择不同的图形进行绘画
    def choose_graph(self):
        graph_index = self.graphoto1.currentText()
        if graph_index == '画线':
            self.My_Paper.Draw = '画线'
        elif graph_index == '圆形':
            self.My_Paper.Draw = '圆形'
        elif graph_index == '矩形':
            self.My_Paper.Draw = '矩形'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = window()
    mainwindow.show()
    sys.exit(app.exec_())
