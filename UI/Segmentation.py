from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtGui import QPixmap


class Segmentation(QWidget):
    def __init__(self):
        super(Segmentation, self).__init__()
        self.init()
        self.init_layers()

    def init(self):
        self.setFixedWidth(400)
        self.setFixedHeight(300)

    def init_layers(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        top_layout = QGridLayout()
        main_layout.addLayout(top_layout)
        middle_layout = QGridLayout()
        main_layout.addLayout(middle_layout)

        title_label = QLabel('这是语义分割')
        top_layout.addWidget(title_label, 0, 0)
        select_image_btn = QPushButton('选择单张图片')
        top_layout.addWidget(select_image_btn, 1, 0)
        select_image_btn.clicked.connect(self.open_single_file)
        select_images_btn = QPushButton('选择文件夹')
        top_layout.addWidget(select_images_btn, 1, 1)
        select_images_btn.clicked.connect(self.open_folder)

        self.input_image = QLabel()
        middle_layout.addWidget(self.input_image, 0, 0)
        self.output_image = QLabel()
        middle_layout.addWidget(self.output_image, 0, 1)

    def open_single_file(self):
        file_path = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择你要上传的图片",  # 标题
            r"d:\\data",  # 起始目录
            "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        file_path = file_path[0]
        print(file_path)
        self.input_image.setPixmap(QPixmap(file_path))
        # 图片大小与label适应，否则图片可能显示不全
        self.input_image.setScaledContents(True)

    def open_folder(self):
        file_paths = QFileDialog.getExistingDirectory(
            self,  # 父窗口对象
            "选择你要上传的图片",  # 标题
        )
        print(file_paths)
