from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel

from classes.imagepp import ImagePP


class MainInterface(QWidget):

    def __init__(self):
        super().__init__()
        print("in main interface")
        self.open_file_btn = QPushButton("Open the file")
        self.open_id_btn = QPushButton("Enter")

        self.id_le = QLineEdit()

        self.picture_lbl = QLabel()

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.imgpp = ImagePP(id="27")
        self.settings()

    def settings(self):
        self.picture_lbl.setPixmap(QPixmap(self.imgpp.get_original_path()).scaledToWidth(300))
        self.picture_lbl.show()
        self.picture_lbl.setScaledContents(True)

        self.vbox.addWidget(self.open_file_btn)
        self.hbox.addWidget(self.id_le)
        self.hbox.addWidget(self.open_id_btn)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.picture_lbl)
        self.setLayout(self.vbox)