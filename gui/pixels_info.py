from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy, \
    QFileDialog

from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_info import PPInfo
from gui.picture_info import PictureInfo
from services.picture_main_service import PictureMainService


class PixelsInfo(QWidget):

    def __init__(self):
        super().__init__()

        self.open_picture_btn = PPButton(self, "default")
        self.add_picture_btn = PPButton(self, "default")

        self.pp_all_pixels_info = PPInfo()
        self.pp_painted_pixels_info = PPInfo()
        self.pp_remaining_pixels_info = PPInfo()

        self.picture_window = PictureInfo()

        self.hbox_buttons = QHBoxLayout()
        self.hbox_info = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self._settings()

    def _settings(self):

        self.open_picture_btn.setText("Open picture")
        self.open_picture_btn.clicked.connect(self.open_picture)
        self.open_picture_btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        self.add_picture_btn.setText("Add picture")
        self.add_picture_btn.clicked.connect(self.add_new_picture)
        self.add_picture_btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        self.pp_all_pixels_info.set_label("All pixels")
        self.pp_all_pixels_info.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.pp_painted_pixels_info.set_label("Painted pixels")
        self.pp_painted_pixels_info.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.pp_remaining_pixels_info.set_label("Remaining pixels")
        self.pp_remaining_pixels_info.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

        self.update_pixels_info()

        self.picture_window.upd_current_picture.connect(self.update_pixels_info)

        self.hbox_buttons.setSpacing(20)
        self.hbox_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.hbox_buttons.addWidget(self.open_picture_btn)
        self.hbox_buttons.addWidget(self.add_picture_btn)

        self.hbox_info.setSpacing(20)
        self.hbox_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.hbox_info.addWidget(self.pp_all_pixels_info)
        self.hbox_info.addWidget(self.pp_painted_pixels_info)
        self.hbox_info.addWidget(self.pp_remaining_pixels_info)

        self.vbox.setContentsMargins(0,0,0,0)
        self.vbox.setSpacing(20)
        self.vbox.addLayout(self.hbox_buttons)
        self.vbox.addLayout(self.hbox_info)

        self.setLayout(self.vbox)

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
        self.pp_all_pixels_info.set_value(f"{pic_info.all_pixels}")
        self.pp_painted_pixels_info.set_value(f"{pic_info.opened_pixels}")
        remaining_pixels = pic_info.all_pixels - pic_info.opened_pixels
        self.pp_remaining_pixels_info.set_value(f"{remaining_pixels}")

        self.picture_window.update_all_info()

    def close_windows(self):
        self.picture_window.close()