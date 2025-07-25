import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class plugin_path:
    def path(self):
        # 设置插件路径的，如果打包成app可以去掉,需要按照本机实际情况修改绝对路径
        import os
        os.environ[
            "QT_QPA_PLATFORM_PLUGIN_PATH"] = r"C:\Users\Newland\Desktop\物联网大赛\开发\Python\python大赛1\大赛1\Lib\site-packages\PyQt5\Qt5\plugins\platforms"


class WindowInit:
    def __init__(self, title="", resize_w=600, resize_h=400):
        self.title = title  # 存储标题
        self.resize_w = resize_w    # 存储画布大小
        self.resize_h = resize_h

    def windowinit(self):
        app = QApplication(sys.argv)
        w = QWidget()
        w.setWindowTitle(self.title)
        w.setWindowIcon(QIcon('06_icon.png'))  # 设置窗口图标
        screen_center = QDesktopWidget().availableGeometry().center()
        w.move(
            screen_center.x() - self.resize_w // 2,  # 水平居中
            screen_center.y() - self.resize_h // 2  # 垂直居中
        )
        w.resize(self.resize_w, self.resize_h)
        w.show()
        app.exec()

class  WindowInit_2(QWidget):
    def __init__(self, title="", resize_w=600, resize_h=400):
        super().__init__()
        self.title = title  # 存储标题
        self.resize_w = resize_w  # 存储画布大小
        self.resize_h = resize_h

    def windowinit_2(self):
        app = QApplication(sys.argv)
        w = QWidget()
        w.setWindowTitle(self.title)
        w.setWindowIcon(QIcon('06_icon.png'))  # 设置窗口图标
        screen_center = QDesktopWidget().availableGeometry().center()
        w.move(
            screen_center.x() - self.resize_w // 2,  # 水平居中
            screen_center.y() - self.resize_h // 2  # 垂直居中
        )
        w.resize(self.resize_w, self.resize_h)
        w.show()
        app.exec()
