from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy, \
    QFileDialog

from gui.picture_info import PictureInfo
from services.picture_main_service import PictureMainService


class PixelsInfo(QWidget):

    def __init__(self):
        super().__init__()

        self.open_picture_btn = QPushButton()
        self.add_picture_btn = QPushButton()

        self.opened_info_lbl = QLabel()
        self.opened_value_lbl = QLabel()
        self.left_info_lbl = QLabel()
        self.left_value_lbl = QLabel()

        self.picture_window = PictureInfo()

        self.hbox = QHBoxLayout()
        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self._settings()

    def _settings(self):

        self.setStyleSheet("background-color:gray")

        self.open_picture_btn.setText("Open picture")
        self.open_picture_btn.clicked.connect(self.open_picture)

        self.add_picture_btn.setText("Add picture")
        self.add_picture_btn.clicked.connect(self.add_new_picture)

        self.opened_info_lbl.setText("Painter pixels:")
        self.left_info_lbl.setText("Left pixels:")
        self.update_pixels_info()

        self.picture_window.upd_current_picture.connect(self.update_pixels_info)

        self.hbox.addWidget(self.open_picture_btn)
        self.hbox.addWidget(self.add_picture_btn)

        self.grid.addWidget(self.opened_info_lbl, 0, 0)
        self.grid.addWidget(self.opened_value_lbl, 0, 1)
        self.grid.addWidget(self.left_info_lbl, 1, 0)
        self.grid.addWidget(self.left_value_lbl, 1, 1)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.grid)

        self.setLayout(self.vbox)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def open_picture(self):
        self.picture_window.reset_widget()
        self.picture_window.show()

    def add_new_picture(self):
        pic_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select a picture (jpg, png)",
            "",
            "Image files (*.jpg *.jpeg *.png) |*.jpg; *.jpeg; *.png"
        )
        if pic_path:
            PictureMainService.add_new_picture(pic_path)
            self.update_pixels_info()

    def update_pixels_info(self):
        pic_info = PictureMainService.get_picture_info()
        self.opened_value_lbl.setText(f"{pic_info.opened_pixels}")
        left_pixels = pic_info.all_pixels - pic_info.opened_pixels
        self.left_value_lbl.setText(f"{left_pixels}")

        self.picture_window.update_all_info()

    def close_windows(self):
        self.picture_window.close()