import os

import psutil
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy, \
    QFileDialog

from services.base_main_service import BaseMainService
from services.picture_main_service import PictureMainService
from utilits.filename_utilits import check_filename
from utilits.image_utilits import resource_path


class CreateSave(QWidget):

    current_save_chosen = pyqtSignal(str)

    saves = []
    save_buttons = []
    picture_path = ""

    def __init__(self):
        #print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

        super().__init__()

        self.saves_container = QWidget()
        self.saves_vbox = QVBoxLayout(self.saves_container)
        self.scroll_area = QScrollArea()

        self.logo = QLabel()
        self.pixmap = QPixmap()

        self.save_title_le = QLineEdit()

        self.add_picture_lbl = QLabel()
        self.add_picture_btn = QPushButton()

        self.create_btn = QPushButton()

        self.create_vbox = QVBoxLayout()
        self.picture_hbox = QHBoxLayout()
        self.hbox = QHBoxLayout()

        self._settings()

    def _settings(self):

        self._create_list_of_saves()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.saves_container)
        self.scroll_area.setFixedHeight(300)

        self.pixmap = QPixmap.fromImage(QImage(resource_path("logo.png")))
        self.pixmap = self.pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo.setPixmap(self.pixmap)
        self.logo.setMaximumHeight(100)

        self.add_picture_lbl.setText("No picture")
        self.add_picture_btn.setText("Add Picture")
        self.add_picture_btn.clicked.connect(self._add_picture)

        self.create_btn.setText("Create Save")
        self.create_btn.clicked.connect(self._create_save)

        self.picture_hbox.addWidget(self.add_picture_lbl)
        self.picture_hbox.addWidget(self.add_picture_btn)

        self.create_vbox.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.create_vbox.addWidget(self.save_title_le)
        self.create_vbox.addLayout(self.picture_hbox)
        self.create_vbox.addWidget(self.create_btn)

        if len(self.saves) != 0:
            self.hbox.addWidget(self.scroll_area)
        widget = QWidget()
        widget.setMaximumHeight(300)
        widget.setLayout(self.create_vbox)
        self.hbox.addWidget(widget)

        self.setLayout(self.hbox)

    def _create_list_of_saves(self):
        self.saves = BaseMainService.get_saves()
        self.save_buttons = []
        for index, save in enumerate(self.saves):
            save_button = QPushButton()
            save_button.setText(save)
            self.save_buttons.append(save_button)
            self.save_buttons[index].clicked.connect(lambda: self._open_save(self.sender().text()))
            self.saves_vbox.addWidget(self.save_buttons[index], alignment=Qt.AlignmentFlag.AlignTop)

    def _add_picture(self):
        pic_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select a picture (jpg, jpeg, png)",
            "",
            "Image files (*.jpg *.jpeg *.png) |*.jpg; *.jpeg; *.png"
        )
        if pic_path:
            self.picture_path = pic_path
            self.add_picture_lbl.setText(self.picture_path)

    def _open_save(self, title):
        self.current_save_chosen.emit(title)
        self.close()

    def _create_save(self): #TODO: check if title is creatable, forbidden symbols
        if self.save_title_le.text() == "" or self.save_title_le.text() in self.saves:
            return
        if self.picture_path == "":
            return
        title = self.save_title_le.text().strip()
        if not check_filename(title):
            return

        BaseMainService.create_new_save(title)
        PictureMainService.add_new_picture(self.picture_path)
        self._open_save(title)

