from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QSizePolicy, QPushButton, QHBoxLayout, \
    QMessageBox

from consts import BACKGROUND_DARKER, BACKGROUND
from enums.status_enum import StatusEnum
from gui.custom_widgets.pp_icon_button import PPIconButton
from gui.custom_widgets.pp_info import PPInfo
from gui.custom_widgets.scalable_label import ScalableLabel
from gui.custom_widgets.status_label import StatusLabel
from gui.custom_widgets.pp_status_bar import PPStatusBar
from services.picture_main_service import PictureMainService
from services.save_main_service import SaveMainService
from utilits.image_utilits import resource_path


class PictureInfo(QWidget):
    # to update info in pixels_info when current picture is changed
    upd_current_picture = pyqtSignal()

    current_id = 0
    active_id = 0
    pictures_ids = []

    def __init__(self):
        super().__init__()

        self.status_label = StatusLabel()
        self.status_bar = PPStatusBar(self, StatusEnum.STOPPED)

        self.left_btn = PPIconButton("default", "left")
        self.right_btn = PPIconButton("default", "right")

        self.picture = ScalableLabel()
        self.pixmap = QPixmap()

        self.pp_all_pixels_info = PPInfo()
        self.pp_painted_pixels_info = PPInfo()
        self.pp_remaining_pixels_info = PPInfo()

        self.delete_btn = PPIconButton("stroke", "delete")

        self.hbox_status = QHBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox_info = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self._settings()
        self.set_css()

    def _settings(self):
        self.setWindowTitle("Pictures information")
        self.resize(400, 400)

        self.active_id = PictureMainService.get_picture_info().id
        self.current_id = self.active_id
        self.pictures_ids = SaveMainService.get_pictures_ids()

        self.left_btn.clicked.connect(lambda: self._change_picture("left"))
        self.right_btn.clicked.connect(lambda: self._change_picture("right"))
        self._check_possibilities_to_move()

        self.picture.setMinimumSize(200, 200)
        self.picture.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.update_progress_picture()

        self.status_label.clicked.connect(self._update_current_picture)
        self.update_status_label()

        self.hbox_status.addWidget(self.status_label)

        self.hbox.setContentsMargins(0,0,0,0)
        self.hbox.addWidget(self.left_btn)
        self.hbox.addWidget(self.picture)
        self.hbox.addWidget(self.right_btn)

        self.pp_all_pixels_info.set_label("All pixels")
        self.pp_painted_pixels_info.set_label("Painted pixels")
        self.pp_remaining_pixels_info.set_label("Remaining pixels")

        self.update_pixels_info()

        self.delete_btn.clicked.connect(self._delete_picture)

        self.hbox_info.setSpacing(20)
        self.hbox_info.setContentsMargins(20,10,20,10)
        self.hbox_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.hbox_info.addWidget(self.pp_all_pixels_info)
        self.hbox_info.addWidget(self.pp_painted_pixels_info)
        self.hbox_info.addWidget(self.pp_remaining_pixels_info)
        self.hbox_info.addStretch()
        self.hbox_info.addWidget(self.delete_btn)

        widget = QWidget()
        widget.setLayout(self.hbox_info)
        widget.setStyleSheet(f"""
            background-color: {BACKGROUND_DARKER};
            border-radius: 10px;
        """)

        self.vbox.addWidget(self.status_bar)
        self.vbox.addLayout(self.hbox_status)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(widget)

        self.setLayout(self.vbox)

    def set_css(self):
        self.setStyleSheet(f"""
            PictureInfo
            {{
                background-color: {BACKGROUND};
            }}
        """)

    def update_progress_picture(self):
        ppic = PictureMainService.get_progress_picture(self.active_id)
        self.pixmap = QPixmap.fromImage(ppic)
        self.resizeEvent(None)

    def update_pixels_info(self):
        pic_info = PictureMainService.get_picture_info(self.active_id)
        self.pp_all_pixels_info.set_value(f"{pic_info.all_pixels}")
        self.pp_painted_pixels_info.set_value(f"{pic_info.opened_pixels}")
        remaining_pixels = pic_info.all_pixels - pic_info.opened_pixels
        self.pp_remaining_pixels_info.set_value(f"{remaining_pixels}")


    def update_status_label(self):
        pic_info = PictureMainService.get_picture_info(self.active_id)
        if pic_info.status == StatusEnum.FINISHED:
            self.status_label.setText("Finished")
            self.status_label.set_status_color("GrEen")
        elif pic_info.status == StatusEnum.IN_PROGRESS:
            self.status_label.setText("IN PROGRESS")
            self.status_label.set_status_color("red")
        else:
            self.status_label.setText("STOPPED")
            self.status_label.set_status_color("velvet")

    def update_all_info(self):
        self.update_progress_picture()
        self.update_pixels_info()
        self.update_status_label()
        self._check_possibilities_to_move()
        self._check_possibilities_to_delete()

    def _update_current_picture(self):
        pic_info = PictureMainService.get_picture_info(self.active_id)
        if pic_info.all_pixels != pic_info.opened_pixels and self.current_id != self.active_id:
            reply = QMessageBox.question(self, "Set new current picture", "Are you sure?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.current_id = self.active_id
                PictureMainService.update_current_picture_id(self.current_id)
                self.update_all_info()
                self.upd_current_picture.emit()

    def resizeEvent(self, event):
        if hasattr(self, 'pixmap'):
            scaled = self.pixmap.scaled(self.picture.contentsRect().size(),
                                   Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)
            self.picture.setPixmap(scaled)

    def reset_widget(self):
        self.active_id = PictureMainService.get_picture_info().id
        self.current_id = SaveMainService.get_current_picture_id()
        self.pictures_ids = SaveMainService.get_pictures_ids()
        self.update_all_info()

    def _change_picture(self, move):
        if move == "right":
            ind = self.pictures_ids.index(self.active_id)
            self.active_id = self.pictures_ids[ind + 1]
        elif move == "left":
            ind = self.pictures_ids.index(self.active_id)
            self.active_id = self.pictures_ids[ind - 1]
        self.update_all_info()

    def _delete_picture(self):
        if len(self.pictures_ids) < 2:
            return

        reply = QMessageBox.question(self, "Delete this picture?", "Are you sure?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            return

        delete_id = self.active_id

        if self.active_id == self.current_id:
            new_c_id = PictureMainService.find_new_current_picture()
            self.current_id = new_c_id
            self.active_id = self.current_id
            PictureMainService.update_current_picture_id(self.current_id)
            self.update_all_info()
            self.upd_current_picture.emit()
        else:
            if self.right_btn.isEnabled():
                ind = self.pictures_ids.index(self.active_id)
                self.active_id = self.pictures_ids[ind + 1]
            else:
                ind = self.pictures_ids.index(self.active_id)
                self.active_id = self.pictures_ids[ind - 1]
            self.update_all_info()

        PictureMainService.delete_picture(delete_id)
        self.pictures_ids = SaveMainService.get_pictures_ids()
        self.update_all_info()

    def _check_possibilities_to_move(self):
        self.left_btn.setEnabled(True)
        self.right_btn.setEnabled(True)
        if self.pictures_ids.index(self.active_id) == 0:
            self.left_btn.setEnabled(False)
        if self.pictures_ids.index(self.active_id) == len(self.pictures_ids) - 1:
            self.right_btn.setEnabled(False)

    def _check_possibilities_to_delete(self):
        self.delete_btn.setEnabled(True)
        if len(self.pictures_ids) < 2:
            self.delete_btn.setEnabled(False)
