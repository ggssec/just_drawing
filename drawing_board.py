# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '试样.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import cv2
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
from tuoyuan import *
import json
import os
import copy
from PyQt5 import QtCore, QtGui, QtWidgets
from paint_part import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(794, 597)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_width = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_width.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_width)
        self.pushButton_color = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_color.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_color)
        self.pushButton_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton_clear)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_5 = QtWidgets.QMenu(self.menu)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menu)
        self.menu_6.setObjectName("menu_6")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_dxf = QtWidgets.QAction(mainWindow)
        self.action_dxf.setObjectName("action_dxf")
        self.action_4 = QtWidgets.QAction(mainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(mainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(mainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(mainWindow)
        self.action_7.setObjectName("action_7")
        self.menu_5.addAction(self.action_dxf)
        self.menu_5.addAction(self.action_4)
        self.menu_6.addAction(self.action_5)
        self.menu_6.addAction(self.action_6)
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_6.menuAction())
        self.menu_3.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())



        self.My_Area = My_Board(mainWindow)
        self.My_Area.setGeometry(180, 40, 601, 501)

        self.retranslateUi(mainWindow)

        self.pushButton_clear.clicked.connect(self.paint_BoardClear)
        self.pushButton_width.clicked.connect(self.choose_width)
        self.pushButton_color.clicked.connect(self.choose_color)
        self.action_5.triggered.connect(self.save_pic)
        self.action_4.triggered.connect(self.creatweb)
        self.action_dxf.triggered.connect(self.opendxf)
        self.comboBox.currentIndexChanged.connect(self.choose_graph)

        QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.pushButton_width.setText(_translate("mainWindow", "画笔粗细"))
        self.pushButton_color.setText(_translate("mainWindow", "画板颜色"))
        self.pushButton_clear.setText(_translate("mainWindow", "清空画板"))
        self.comboBox.setItemText(0, _translate("mainWindow", "画线"))
        self.comboBox.setItemText(1, _translate("mainWindow", "矩形"))
        self.comboBox.setItemText(2, _translate("mainWindow", "椭圆"))
        self.menu.setTitle(_translate("mainWindow", "文件"))
        self.menu_5.setTitle(_translate("mainWindow", "打开"))
        self.menu_6.setTitle(_translate("mainWindow", "保存"))
        self.menu_3.setTitle(_translate("mainWindow", "工具"))
        self.action.setText(_translate("mainWindow", "关于软件"))
        self.action_dxf.setText(_translate("mainWindow", "打开dxf文件"))
        self.action_4.setText(_translate("mainWindow", "打开网格数据"))
        self.action_5.setText(_translate("mainWindow", "保存图片"))
        self.action_6.setText(_translate("mainWindow", "保存网格数据"))
        self.action_7.setText(_translate("mainWindow", "生成网格"))

        mainWindow.statusBar().showMessage('                                    坐标')
        mainWindow.statusBar().show()
        mainWindow.Board_Coordinates = QLabel('')
        mainWindow.statusBar().addPermanentWidget(mainWindow.Board_Coordinates)


    def opendxf(self):

        savePath = QFileDialog.getOpenFileName(None, '选择文件', '.\\', '*.dxf')
        print(savePath[0])

    def creatweb(self):
        # # fpath = QFileDialog.getOpenFileName(self, "选择文件", ".")
        # # Realpath = os.path.split(fpath[-2])[:-1]
        # # os.chdir(Realpath[0]) # 修改读取图片的路径
        # # fname = os.path.split(fpath[-2])[-1]
        # # img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
        #
        # root = tk.Tk()
        # root.withdraw()
        # Filepath = filedialog.askopenfilename()  # 获得选好的文件
        # img = cv_imread(Filepath)
        #
        # img1 = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)  # 将图片显示为原来的60%
        # # cv2.namedWindow(img,cv2.WINDOW_NORMAL)
        # cv2.imshow('IMREAD_GRAYSCALE+Color', img1)
        # self.h, self.w = img.shape[:]
        # # self.h, self.w = 700,500
        #
        # self.num_edges = 1  # 多边形的边数
        # cv2.waitKey(0)
        self.box = QMessageBox(QMessageBox.Question, '选择', '选择图形', QMessageBox.NoButton)
        self.choice1 = self.box.addButton('正放矩形', QMessageBox.YesRole)
        self.choice2 = self.box.addButton('正放椭圆形', QMessageBox.YesRole)
        self.choice3 = self.box.addButton('多边形', QMessageBox.YesRole)
        self.choice4 = self.box.addButton('斜放矩形', QMessageBox.YesRole)
        self.box.show()

        self.choice1.clicked.connect(lambda: self.bt_choice1())
        self.choice2.clicked.connect(lambda: self.bt_choice2())
        # self.choice3.clicked.connect(lambda: self.bt_choice3())
        # self.choice4.clicked.connect(lambda: self.bt_choice4())

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

    def bt_choice1(self):

        plots = np.array(self.My_Area.coord_rect)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def bt_choice2(self):

        plots = tuoyuan(self.My_Area.coord_elli, self.My_Area.elli_long, self.My_Area.elli_short,50,50)
        plots.mesh(5)

    def bt_choice3(self):

        plots = np.array(self.My_Area.coord_rect)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def bt_choice4(self):

        plots = np.array(self.My_Area.coord_rect)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def save_pic(self):
        savePath = QFileDialog.getSaveFileName(None, 'Save Your Paint', '.\\', '*.png')
        print(savePath)
        # if savePath[0] == "":
        #     print("Save cancel")
        #     return
        image = self.My_Area.GetContentAsQImage()
        image.save(savePath[0])

    def choose_color(self):
        Color = QColorDialog.getColor()  # color是Qcolor
        if Color.isValid():
            self.My_Area.Color = Color

        # 选择画笔粗细

    def choose_width(self):

        width, ok = QInputDialog.getInt(mainWindow, '选择画笔粗细', '请输入粗细：', min=1, step=1)
        if ok:
            self.My_Area.penwidth = width

        # 清空画板

    def paint_BoardClear(self):
        self.My_Area._IfEmpty = 0
        self.My_Area.pixmap.fill(Qt.white)
        mainWindow.update()

        # 选择不同的图形进行绘画

    def choose_graph(self):
        graph_index = self.comboBox.currentText()
        if graph_index == '画线':
            self.My_Area.Draw = '画线'
        elif graph_index == '圆形':
            self.My_Area.Draw = '圆形'
        elif graph_index == '矩形':
            self.My_Area.Draw = '矩形'
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())