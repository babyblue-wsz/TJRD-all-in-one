from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton


class Segmentation(QWidget):
    def __init__(self):
        super(Segmentation, self).__init__()
        self.init_layers()

    def init_layers(self):
        main = QVBoxLayout()
        self.setLayout(main)

        text1 = QLabel('这是语义分割')
        btn = QPushButton('btn')
        main.addWidget(text1)
        main.addWidget(btn)

