from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QSizePolicy, QWIDGETSIZE_MAX

from gui.scalable_label import ScalableLabel
from services.picture_main_service import PictureMainService


class PictureInfo(QWidget):

    def __init__(self):
        super().__init__()

        self.picture = ScalableLabel()
        self.pixmap = QPixmap()

        self.opened_info_lbl = QLabel()
        self.opened_value_lbl = QLabel()
        self.left_info_lbl = QLabel()
        self.left_value_lbl = QLabel()
        self.all_info_lbl = QLabel()
        self.all_value_lbl = QLabel()

        self.grid = QGridLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):

        self.picture.setMinimumSize(200, 100)
        self.picture.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.picture.setStyleSheet("border: 1px solid red; padding: 2px;")
        self.update_progress_picture()

        self.opened_info_lbl.setText("Painter pixels:")
        self.left_info_lbl.setText("Left pixels:")
        self.all_info_lbl.setText("All pixels:")

        self.grid.addWidget(self.opened_info_lbl, 0, 0)
        self.grid.addWidget(self.opened_value_lbl, 0, 1)
        self.grid.addWidget(self.left_info_lbl, 1, 0)
        self.grid.addWidget(self.left_value_lbl, 1, 1)
        self.grid.addWidget(self.all_info_lbl, 2, 0)
        self.grid.addWidget(self.all_value_lbl, 2, 1)

        self.vbox.addWidget(self.picture, stretch=1)
        self.vbox.addLayout(self.grid)

        self.setLayout(self.vbox)

    def update_progress_picture(self):
        ppic = PictureMainService.get_progress_picture()
        self.pixmap = QPixmap.fromImage(ppic)
        self.resizeEvent(None)

    def update_pixels_info(self):
        pic_info = PictureMainService.get_picture_info()
        self.opened_value_lbl.setText(f"{pic_info.opened_pixels}")
        all_pixels = pic_info.all_pixels
        self.all_value_lbl.setText(f"{all_pixels}")
        left_pixels = all_pixels - pic_info.opened_pixels
        self.left_value_lbl.setText(f"{left_pixels}")

    def resizeEvent(self, event):
        if hasattr(self, 'pixmap'):
            scaled = self.pixmap.scaled(self.picture.contentsRect().size(),
                                   Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
            self.picture.setPixmap(scaled)