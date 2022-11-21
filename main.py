import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QAction, QStackedLayout, QGridLayout, QLabel, \
    QPushButton, QWidget, QPlainTextEdit
from PyQt5.QtGui import QIcon
from UI.Segmentation import Segmentation
from UI.OriginMainWindow import OriginMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
        self.set_menu_bar()

    def init(self):
        self.setWindowTitle('TJRD all in one')
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("/Static/tongji.jpg"))

        originMainWindow = OriginMainWindow()
        self.setCentralWidget(originMainWindow)

    def set_menu_bar(self):
        # 创建顶部菜单栏。addMenu()函数创建一级，addAction()函数创建子菜单。
        self.origin = self.menuBar().addMenu('初始')
        self.settings = QAction('设置', self)
        self.count = QAction('账户', self)
        self.origin.addAction(self.settings)
        self.origin.addAction(self.count)

        self.functions = self.menuBar().addMenu('工具箱')
        self.segmentation = QAction('语义分割', self)
        self.recognition = QAction('图像识别', self)
        self.functions.addAction(self.segmentation)
        self.functions.addAction(self.recognition)
        segmentationUI = Segmentation()
        self.segmentation.triggered.connect(lambda: self.show_child_UI(segmentationUI))

    def show_child_UI(self, childUI):
        self.setCentralWidget(childUI)


if __name__ == "__main__":
    # sys.argv是继续接收命令行指令用的
    app = QApplication(sys.argv)
    main_window = MyWidget()
    main_window.show()
    sys.exit(app.exec())
