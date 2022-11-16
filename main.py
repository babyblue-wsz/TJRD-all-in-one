import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QIcon


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_layers()
        self.menu_bar()

    def init_layers(self):
        self.setWindowTitle('TJRD all in one')
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("/Static/tongji.jpg"))
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.show()

    def menu_bar(self):
        origin = self.menuBar().addMenu('初始')
        origin.addAction('设置')
        origin.addAction('账户')
        functions = self.menuBar().addMenu('工具箱')
        functions.addAction('语义分割')
        functions.addAction('图像识别')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec())
