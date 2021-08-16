from drawing_board import *
from web_window import *
import sys


class First_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_mainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.action_9.triggered.connect(self.sub_show)
        self.kid_dialog = Second_window()

        # run_den = self.kid_dialog.sub_ui.midu
        self.kid_dialog.sub_ui.pushButton.clicked.connect(lambda: self.main_ui.bt_choice1(self.main_ui.img))
        self.kid_dialog.sub_ui.pushButton_2.clicked.connect(lambda: self.main_ui.bt_choice2(self.main_ui.img))
        self.kid_dialog.sub_ui.pushButton_3.clicked.connect(lambda: self.main_ui.bt_choice3(self.main_ui.img))
        self.kid_dialog.sub_ui.radioButton_2.toggled.connect(lambda: self.main_ui.define_midu(40))
        self.kid_dialog.sub_ui.radioButton_3.toggled.connect(lambda: self.main_ui.define_midu(20))
        self.kid_dialog.sub_ui.radioButton_4.toggled.connect(lambda: self.main_ui.define_midu(10))
        self.kid_dialog.sub_ui.radioButton.toggled.connect(
            lambda: self.main_ui.define_midu(self.kid_dialog.sub_ui.midu))
        self.kid_dialog.sub_ui.pushButton_4.clicked.connect(self.main_ui.pic_web)

    def sub_show(self):
        self.kid_dialog.show()


class Second_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.sub_ui = Ui_Dialog()
        self.sub_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = First_window()
    child = Second_window()

    # 通过生成网格按钮将两个窗体关联
    # spark=window.main_ui.action_2
    # spark.triggered.connect(child.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
