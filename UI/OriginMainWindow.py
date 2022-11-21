from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class OriginMainWindow(QWidget):
    def __init__(self):
        super(OriginMainWindow, self).__init__()
        self.init_layers()

    def init_layers(self):
        main = QVBoxLayout()
        self.setLayout(main)
        text1 = QLabel('这是初始默认界面')
        main.addWidget(text1)
