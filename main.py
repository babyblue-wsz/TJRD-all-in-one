import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QAction, QStackedLayout
from PyQt5.QtGui import QIcon
from UI.Segmentation import Segmentation
from UI.Color import Color


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_layers()
        self.menu_bar()

    def init_layers(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.setWindowTitle('TJRD all in one')
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("/Static/tongji.jpg"))

        self.stacked_layouts = QStackedLayout()
        self.main_layout.addLayout(self.stacked_layouts)

        segmentationUI = Segmentation()
        self.stacked_layouts.addWidget(segmentationUI)

        # print(self.stacked_layouts.currentIndex())

    def menu_bar(self):
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

        # self.segmentation.triggered.connect(self.show_segmentationUI)

    def show_segmentationUI(self):
        self.stacked_layouts.setCurrentIndex(0)

if __name__ == "__main__":
    # sys.argv是继续接收命令行指令用的
    # app = QApplication(sys.argv)
    app = QApplication([])
    main_window = MyWidget()
    main_window.show()
    sys.exit(app.exec())
