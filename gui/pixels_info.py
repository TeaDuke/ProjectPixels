from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy

from gui.picture_info import PictureInfo


class PixelsInfo(QWidget):

    def __init__(self):
        super().__init__()

        self.open_picture_btn = QPushButton(self)
        self.change_picture_btn = QPushButton(self)

        self.painted_info_lbl = QLabel(self)
        self.painted_value_lbl = QLabel(self)
        self.left_info_lbl = QLabel(self)
        self.left_value_lbl = QLabel(self)

        self.picture_window = PictureInfo(self)

        self.hbox = QHBoxLayout(self)
        self.grid = QGridLayout(self)
        self.vbox = QVBoxLayout(self)
        self._settings()

    def _settings(self):

        self.setStyleSheet("background-color:gray")

        self.open_picture_btn.setText("Open picture")
        self.open_picture_btn.clicked.connect(self.open_picture)

        self.change_picture_btn.setText("Add picture")

        self.painted_info_lbl.setText("Painter pixels:")
        self.painted_value_lbl.setText("0 (hard)")
        self.left_info_lbl.setText("Left pixels:")
        self.left_value_lbl.setText("10 (hard)")

        self.hbox.addWidget(self.open_picture_btn)
        self.hbox.addWidget(self.change_picture_btn)

        self.grid.addWidget(self.painted_info_lbl, 0, 0)
        self.grid.addWidget(self.painted_value_lbl, 0, 1)
        self.grid.addWidget(self.left_info_lbl, 1, 0)
        self.grid.addWidget(self.left_value_lbl, 1, 1)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.grid)

        self.setLayout(self.vbox)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def open_picture(self):
        self.picture_window.show()