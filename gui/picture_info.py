from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QSizePolicy, QPushButton, QHBoxLayout, \
    QMessageBox

from gui.custom_widgets.scalable_label import ScalableLabel
from gui.custom_widgets.status_label import StatusLabel
from services.picture_main_service import PictureMainService
from services.save_main_service import SaveMainService


class PictureInfo(QWidget):
    upd_current_picture = pyqtSignal()

    current_id = 0
    active_id = 0
    pictures_ids = []

    def __init__(self):
        super().__init__()

        self.status_label = StatusLabel()

        self.left_btn = QPushButton()
        self.right_btn = QPushButton()

        self.picture = ScalableLabel()
        self.pixmap = QPixmap()

        self.opened_info_lbl = QLabel()
        self.opened_value_lbl = QLabel()
        self.left_info_lbl = QLabel()
        self.left_value_lbl = QLabel()
        self.all_info_lbl = QLabel()
        self.all_value_lbl = QLabel()

        self.hbox_status = QHBoxLayout()

        self.hbox = QHBoxLayout()

        self.grid = QGridLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):

        self.active_id = PictureMainService.get_picture_info().id
        self.current_id = self.active_id
        self.pictures_ids = SaveMainService.get_pictures_ids()

        self.left_btn.setIcon(QIcon("images\\chevron-left.svg"))
        self.left_btn.setIconSize(QSize(48,48))
        self.left_btn.clicked.connect(lambda: self.change_picture("left"))
        self.right_btn.setIcon(QIcon("images\\chevron-right.svg"))
        self.right_btn.setIconSize(QSize(48,48))
        self.right_btn.clicked.connect(lambda: self.change_picture("right"))
        self.check_possibilities_to_move()

        self.picture.setMinimumSize(200, 100)
        self.picture.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.picture.setStyleSheet("border: 1px solid red; padding: 2px;")
        self.update_progress_picture()

        self.status_label.clicked.connect(self.update_current_picture)
        self.update_status_label()

        self.hbox_status.addWidget(self.status_label)

        self.hbox.addWidget(self.left_btn)
        self.hbox.addWidget(self.picture, stretch=1)
        self.hbox.addWidget(self.right_btn)

        self.opened_info_lbl.setText("Painter pixels:")
        self.left_info_lbl.setText("Left pixels:")
        self.all_info_lbl.setText("All pixels:")
        self.update_pixels_info()

        self.grid.addWidget(self.opened_info_lbl, 0, 0)
        self.grid.addWidget(self.opened_value_lbl, 0, 1)
        self.grid.addWidget(self.left_info_lbl, 1, 0)
        self.grid.addWidget(self.left_value_lbl, 1, 1)
        self.grid.addWidget(self.all_info_lbl, 2, 0)
        self.grid.addWidget(self.all_value_lbl, 2, 1)

        self.vbox.addLayout(self.hbox_status)
        self.vbox.addLayout(self.hbox, stretch=1)
        self.vbox.addLayout(self.grid)

        self.setLayout(self.vbox)

    def update_progress_picture(self):
        ppic = PictureMainService.get_progress_picture(self.active_id)
        self.pixmap = QPixmap.fromImage(ppic)
        self.resizeEvent(None)

    def update_pixels_info(self):
        pic_info = PictureMainService.get_picture_info(self.active_id)
        self.opened_value_lbl.setText(f"{pic_info.opened_pixels}")
        all_pixels = pic_info.all_pixels
        self.all_value_lbl.setText(f"{all_pixels}")
        left_pixels = all_pixels - pic_info.opened_pixels
        self.left_value_lbl.setText(f"{left_pixels}")


    def update_status_label(self):
        pic_info = PictureMainService.get_picture_info(self.active_id)
        if pic_info.all_pixels == pic_info.opened_pixels:
            self.status_label.setText("Finished")
            self.status_label.setStatusColor("GrEen")
        elif self.active_id == self.current_id:
            self.status_label.setText("Work (current)")
            self.status_label.setStatusColor("red")
        else:
            self.status_label.setText("Pause")
            self.status_label.setStatusColor("velvet")

    def update_current_picture(self):
        pic_info = PictureMainService.get_picture_info(self.active_id)
        if pic_info.all_pixels != pic_info.opened_pixels and self.current_id != self.active_id:
            reply = QMessageBox.question(self, "Set new current picture", "Are you sure?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.current_id = self.active_id
                PictureMainService.update_current_picture_id(self.current_id)
                self.update_pixels_info()
                self.update_progress_picture()
                self.update_status_label()
                self.upd_current_picture.emit()

    def resizeEvent(self, event):
        if hasattr(self, 'pixmap'):
            scaled = self.pixmap.scaled(self.picture.contentsRect().size(),
                                   Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
            self.picture.setPixmap(scaled)

    def reset_widget(self):
        self.active_id = PictureMainService.get_picture_info().id
        self.pictures_ids = SaveMainService.get_pictures_ids()
        self.update_pixels_info()
        self.update_progress_picture()
        self.update_status_label()
        self.check_possibilities_to_move()

    def change_picture(self, move):
        if move == "right":
            ind = self.pictures_ids.index(self.active_id)
            self.active_id = self.pictures_ids[ind + 1]
        elif move == "left":
            ind = self.pictures_ids.index(self.active_id)
            self.active_id = self.pictures_ids[ind - 1]
        self.update_progress_picture()
        self.update_pixels_info()
        self.update_status_label()
        self.check_possibilities_to_move()

    def check_possibilities_to_move(self):
        if self.pictures_ids.index(self.active_id) == 0:
            self.left_btn.setEnabled(False)
            self.right_btn.setEnabled(True)
        elif self.pictures_ids.index(self.active_id) == len(self.pictures_ids) - 1:
            self.right_btn.setEnabled(False)
            self.left_btn.setEnabled(True)
        else:
            self.left_btn.setEnabled(True)
            self.right_btn.setEnabled(True)
