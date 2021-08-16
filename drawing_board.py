import sys
import dxfgrabber
from polygon import *
from tuoyuan import *
from PyQt5 import QtCore,  QtWidgets
from paint_part import *
import tkinter as tk
from tkinter import filedialog
import functions
from Physical_boundary_acquisition import *
from looking_for_vertices import *
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
        self.action_pic = QtWidgets.QAction(mainWindow)
        self.action_pic.setObjectName("action_pic")
        self.action_spot = QtWidgets.QAction(mainWindow)
        self.action_spot.setObjectName("action_spot")
        self.action_5 = QtWidgets.QAction(mainWindow)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(mainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(mainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(mainWindow)
        self.action_9.setObjectName("action_9")
        self.action_save = QtWidgets.QAction(mainWindow)
        self.action_save.setObjectName("action_save")
        self.menu_5.addAction(self.action_dxf)
        self.menu_5.addAction(self.action_pic)
        self.menu_5.addAction(self.action_spot)
        self.menu_6.addAction(self.action_5)
        self.menu_6.addAction(self.action_save)
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_6.menuAction())
        self.menu_3.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.My_Area = My_Board(mainWindow)
        self.My_Area.setGeometry(180, 40, 601, 501)
        self.retranslateUi(mainWindow)
        self.pushButton_clear.clicked.connect(self.paint_BoardClear)
        self.pushButton_width.clicked.connect(self.choose_width)
        self.pushButton_color.clicked.connect(self.choose_color)
        self.action_5.triggered.connect(self.save_pic)
        self.action_7.triggered.connect(self.creatweb)
        self.action_8.triggered.connect(self.creat_dxfweb)

        self.action_dxf.triggered.connect(self.opendxf)
        self.action_pic.triggered.connect(self.openpic)
        self.action_spot.triggered.connect(self.input_data)
        self.action_save.triggered.connect(self.save_point)
        self.comboBox.currentIndexChanged.connect(self.choose_graph)
        QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "针对多边形和椭圆形的通用式二维图形网格划分软件"))
        self.pushButton_width.setText(_translate("mainWindow", "画笔粗细"))
        self.pushButton_color.setText(_translate("mainWindow", "画笔颜色"))
        self.pushButton_clear.setText(_translate("mainWindow", "清空画板"))
        self.comboBox.setItemText(0, _translate("mainWindow", "画线"))
        self.comboBox.setItemText(1, _translate("mainWindow", "矩形"))
        self.comboBox.setItemText(2, _translate("mainWindow", "椭圆"))
        self.menu.setTitle(_translate("mainWindow", "文件"))
        self.menu_5.setTitle(_translate("mainWindow", "打开文件"))
        self.menu_6.setTitle(_translate("mainWindow", "保存"))
        self.menu_3.setTitle(_translate("mainWindow", "工具"))
        self.action.setText(_translate("mainWindow", "关于软件"))
        self.action_dxf.setText(_translate("mainWindow", "打开dxf文件"))
        self.action_pic.setText(_translate("mainWindow", "打开图片"))
        self.action_spot.setText(_translate("mainWindow", "输入节点数据"))
        self.action_save.setText(_translate("mainWindow", "保存节点数据"))
        self.action_5.setText(_translate("mainWindow", "保存图片"))
        self.action_7.setText(_translate("mainWindow", "生成绘图网格"))
        self.action_8.setText(_translate("mainWindow", "生成dxf网格"))
        self.action_9.setText(_translate("mainWindow", "生成图片网格"))
        self.jie_dian1 = np.array([])
        self.jie_dian2 = np.array([])
        self.jie_dian3 = np.array([])
        self.boundary_coordinates1 = []
        self.boundary_coordinates2 = []
        self.boundary_coordinates3 = []
        mainWindow.statusBar().showMessage('                                    坐标')
        mainWindow.statusBar().show()
        mainWindow.Board_Coordinates = QLabel('')
        mainWindow.statusBar().addPermanentWidget(mainWindow.Board_Coordinates)

    def input_data(self):
        openPath = QFileDialog.getOpenFileName(None, '选择文件', '.\\', '*.npy')
        if openPath[-2]:
            a = np.load(openPath[-2])
            print(openPath[-2])
            functions.drawing(a)


    def save_point(self):
        savePath = QFileDialog.getSaveFileName(None, '选择保存路径', '.\\', '*.npy')
        print(savePath[-2])
        if savePath[-2]:
            if self.jie_dian1.size:
                np.save(savePath[-2], self.jie_dian1)
            if self.jie_dian2.size:
                np.save(savePath[-2], self.jie_dian2)
            if self.jie_dian3.size:
                np.save(savePath[-2], self.jie_dian3)

    #打开图片文件
    def openpic(self):
        root = tk.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename()  # 获得选好的文件
        if Filepath:
            self.img = cv_imread(Filepath)

            img1 = resize(self.img, None, fx=0.6, fy=0.6, interpolation=INTER_AREA)  # 将图片显示为原来的60%
            imshow('IMREAD_GRAYSCALE+Color', img1)
            self.h, self.w = self.img.shape[:]

            self.num_edges = 1  # 多边形的边数
            waitKey(0)


    def opendxf(self):
        self.line = []
        self.circle_c = []
        self.circle_r = []
        self.lwpolyline = []
        self.ellipse_center = []
        self.ellipse_ratio_long = []
        self.ellipse_ratio = []
        self.type_of_entity = []
        dxf_name = QFileDialog.getOpenFileName(None, '选择文件', '.\\', '*.dxf')
        if dxf_name[0]:
            dxf = dxfgrabber.readfile(dxf_name[0])
            for entities in dxf.entities:
                self.type_of_entity.append(entities.dxftype)
            print(self.type_of_entity)
            if self.type_of_entity.count(self.type_of_entity[0]) == len(self.type_of_entity):
                if self.type_of_entity[0] == 'LINE':
                    for entities in dxf.entities:
                        self.line.append(entities.start[:2])
                        self.line.append(entities.end[:2])
                    self.line = set(self.line)
                    print(self.line)
                    self.line1 = list(self.line)
                if self.type_of_entity[0] == 'CIRCLE':
                    for entities in dxf.entities:
                        self.circle_c.append(list(entities.center[:2]))
                        self.circle_r.append(entities.radius)
                    print(self.circle_c)
                    print(self.circle_r)
                if self.type_of_entity[0] == 'LWPOLYLINE':
                    for entities in dxf.entities:
                        self.lwpolyline.append(list(entities.points))
                    print(self.lwpolyline)
                if self.type_of_entity[0] == 'ELLIPSE':
                    for entities in dxf.entities:
                        long_side = math.sqrt((entities.center[0] - entities.major_axis[0]) ** 2 +
                                              (entities.center[1] - entities.major_axis[1]) ** 2)
                        self.ellipse_center.append(list(entities.center)[0:2])
                        self.ellipse_ratio_long.append(long_side)
                        self.ellipse_ratio.append(entities.ratio * long_side)
                    print(
                        self.ellipse_center,
                        self.ellipse_ratio_long,
                        self.ellipse_ratio
                    )
            else:
                QMessageBox.warning(None, '警告', '非单一图形类别', QMessageBox.Yes | QMessageBox.Yes)

    def creat_dxfweb(self):
        self.box_dxf = QMessageBox(QMessageBox.Question, '选择', '选择网格密度', QMessageBox.NoButton)
        choice_high = self.box_dxf.addButton('高', QMessageBox.YesRole)
        choice_middle = self.box_dxf.addButton('中', QMessageBox.YesRole)
        choice_low = self.box_dxf.addButton('低', QMessageBox.YesRole)
        self.box_dxf.show()
        choice_high.clicked.connect(lambda : self.dxf_choice(50,50))
        choice_middle.clicked.connect(lambda: self.dxf_choice(30,30))
        choice_low.clicked.connect(lambda: self.dxf_choice(10, 10))
    def creatweb(self):
        self.box = QMessageBox(QMessageBox.Question, '选择', '选择图形', QMessageBox.NoButton)
        self.choice1 = self.box.addButton('正放矩形', QMessageBox.YesRole)
        self.choice2 = self.box.addButton('正放椭圆形', QMessageBox.YesRole)
        self.box.show()
        self.choice1.clicked.connect(lambda: self.nor_choice1())
        self.choice2.clicked.connect(lambda: self.nor_choice2())
    def dxf_choice(self,m,n):
        if self.type_of_entity[0] == 'LINE':
            plots = np.array(self.line1)
            mesh1 = block_meshing(plots, m, n)
            mesh1.mesh(10)
            plt.show()
        elif self.type_of_entity[0] == 'LWPOLYLINE':
            for i in range(len(self.lwpolyline)):
                plots = np.array(self.lwpolyline[i])
                if plots[0][0] == plots[-1][0]and plots[0][1] == plots[-1][1]:
                    plots = plots[:len(plots) - 1]
                mesh1 = block_meshing(plots, m, n)
                mesh1.mesh(10)
            plt.show()
        elif self.type_of_entity[0] == 'CIRCLE':
            for i in range(len(self.circle_c)):
                plots = tuoyuan(self.circle_c[i],self.circle_c[i]+np.array([self.circle_r[i],0]),self.circle_r[i] ,m, n)
                plots.mesh(5)
            plt.show()
        elif self.type_of_entity[0] == 'ELLIPSE':
            for i in range(len(self.ellipse_center)):
                plots = tuoyuan(self.ellipse_center[i],self.ellipse_center[i]+np.array([self.ellipse_ratio_long[i],0]),
                                self.ellipse_ratio[i] ,m, n)
                plots.mesh(5)
            plt.show()
    def nor_choice1(self):
        for i in range(len(self.My_Area.coord_rect_all)):
            plots = np.array(self.My_Area.coord_rect_all[i])
            if plots[0][0] == plots[-1][0] and plots[0][1] == plots[-1][1]:
                plots = plots[:len(plots) - 1]
            mesh1 = block_meshing(plots, 10, 10)
            mesh1.mesh(10)
        plt.show()
    def nor_choice2(self):
        for i in range(len(self.My_Area.coord_elli_all)):
            plots = tuoyuan(self.My_Area.coord_elli_all[i], self.My_Area.elli_long_all[i],
                            self.My_Area.elli_short_all[i], 10, 10)
            plots.mesh(5)
        plt.show()
    def nor_choice3(self):
        plots = np.array(self.My_Area.coord_rect_all)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)
    def nor_choice4(self):
        plots = np.array(self.My_Area.coord_rect_all)
        mesh1 = block_meshing(plots, 10, 10)
        mesh1.mesh(10)

    def bt_choice1(self, image):

        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_rectangular_1(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        self.boundary_coordinates1 = change_coordinate(self.h, boundary_coordinates)
        boundary_coordinates = rank(boundary_coordinates)
        spots_up = []
        for i in range(len(boundary_coordinates)):
            a = QPoint(boundary_coordinates[i][0], boundary_coordinates[i][1])
            spots_up.append(a)
        self.My_Area.points_up = copy.deepcopy(spots_up)

    def bt_choice2(self, image):

        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_circle(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        self.boundary_coordinates2 = change_coordinate(self.h, boundary_coordinates)
        print(boundary_coordinates)
        self.spots_cir = []
        a = [boundary_coordinates[2][1], boundary_coordinates[0][0]]
        b = [boundary_coordinates[3][1], boundary_coordinates[1][0]]
        self.spots_cir.append(a)
        self.spots_cir.append(b)
        self.My_Area.points_cir = copy.deepcopy(self.spots_cir)
        print(self.My_Area.points_cir)

    def bt_choice3(self, image):
        # web_den = den
        image = Decrease_pixel_density(image)  # 降低像素密度
        looking_for_vertices1 = LookingForVertices(image)  # 新对象
        boundary_coordinates = looking_for_vertices1.Extract_rectangular_2_fast(image)  # 获取顶点坐标信息
        del boundary_coordinates[0]
        self.boundary_coordinates3 = change_coordinate(self.h, boundary_coordinates)
        boundary_coordinates = rank(boundary_coordinates)
        spots_xie = []
        for i in range(len(boundary_coordinates)):
            a = QPoint(boundary_coordinates[i][0], boundary_coordinates[i][1])
            spots_xie.append(a)
        self.My_Area.points_xie = copy.deepcopy(spots_xie)

    def define_midu(self, den):
        self.den = den

    def pic_web(self):
        if self.boundary_coordinates1:
            plots = np.array(self.boundary_coordinates1)
            mesh1 = block_meshing(plots, self.den, self.den)
            self.jie_dian1 = mesh1.mesh(10)
            self.boundary_coordinates1 = []
        elif self.boundary_coordinates2:
            plots = np.array(self.boundary_coordinates2)
            c=[(plots[0][0]+plots[1][0])/2,(plots[0][1]+plots[1][1])/2]
            l = max(abs((plots[0][0]-plots[1][0])/2),abs((plots[2][1]-plots[3][1])/2))
            r = min(abs((plots[0][0]-plots[1][0])/2),abs((plots[2][1]-plots[3][1])/2))
            a = tuoyuan(c,c+np.array([l,0]),r, self.den, self.den)
            # center, r2 = a.feature()
            self.jie_dian2 = a.mesh(5)
            self.boundary_coordinates2 = []
        elif self.boundary_coordinates3:
            plots = np.array(self.boundary_coordinates3)
            mesh1 = block_meshing(plots, self.den, self.den)
            self.jie_dian3 = mesh1.mesh(10)
            self.boundary_coordinates3 = []
    def save_pic(self):
        savePath = QFileDialog.getSaveFileName(None, 'Save Your Paint', '.\\', '*.png')
        print(savePath)
        image = self.My_Area.make_image()
        print(image)
    def choose_color(self):
        Color = QColorDialog.getColor()
        if Color.isValid():
            self.My_Area.Color = Color
    def choose_width(self):
        width, ok = QInputDialog.getInt(None, '选择画笔粗细', '请输入粗细：', min=1, step=1)
        if ok:
            self.My_Area.pen_width = width
    def paint_BoardClear(self):
        self.My_Area._IfEmpty = 0
        self.My_Area.pixmap.fill(Qt.white)
        self.My_Area.update()
    def choose_graph(self):
        graph_index = self.comboBox.currentText()
        if graph_index == '画线':
            self.My_Area.Draw = '画线'
        elif graph_index == '椭圆':
            self.My_Area.Draw = '椭圆'
        elif graph_index == '矩形':
            self.My_Area.Draw = '矩形'
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     ui = Ui_mainWindow()
#     ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())