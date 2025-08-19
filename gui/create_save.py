import os

import psutil
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy, \
    QFileDialog, QGridLayout

from consts import BACKGROUND, BACKGROUND_DARKER, TEXT, TEXT_SIZE
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_enter_value import PPEnterValue
from gui.custom_widgets.pp_lbl_and_btn import PPLblAndBtn
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

        self.save_pp_value = PPEnterValue()

        self.picture_adding = PPLblAndBtn("default")

        self.create_btn = PPButton(self)

        self.create_vbox = QVBoxLayout()
        self.picture_grid = QGridLayout()
        self.hbox = QHBoxLayout()

        self._settings()
        self.set_css()

    def _settings(self):
        self.setWindowTitle("Create or Choose Save")
        self.setMinimumWidth(500)
        self.setMinimumHeight(600)

        self.saves_vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.saves_vbox.setContentsMargins(0,0,0,0)
        self._create_list_of_saves()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.saves_container)
        self.scroll_area.setMinimumHeight(self.height()-100)
        self.scroll_area.setMinimumWidth(200)

        self.pixmap = QPixmap.fromImage(QImage(resource_path("images\\logo.png")))
        # self.pixmap = self.pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo.setPixmap(self.pixmap)
        self.logo.setMaximumHeight(200)

        self.save_pp_value.set_text_to_lbl("Enter Save title:")

        self.picture_adding.set_text_to_lbl("No picture")
        self.picture_adding.set_text_to_btn("Add picture")
        self.picture_adding.btn_clicked.connect(self._add_picture)

        self.create_btn.setText("Create Save")
        self.create_btn.clicked.connect(self._create_save)
        create_btn_hbox = QHBoxLayout()
        create_btn_hbox.setContentsMargins(10,0,10,0)
        create_btn_hbox.addWidget(self.create_btn)

        self.create_vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.create_vbox.setSpacing(20)
        self.create_vbox.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.create_vbox.addSpacing(30)
        self.create_vbox.addWidget(self.save_pp_value)
        self.create_vbox.addWidget(self.picture_adding)
        self.create_vbox.addLayout(create_btn_hbox)

        if len(self.saves) != 0:
            self.hbox.addWidget(self.scroll_area)
        widget = QWidget()
        widget.setMaximumHeight(self.height()-100)
        widget.setMinimumWidth(200)
        widget.setLayout(self.create_vbox)
        self.hbox.addWidget(widget)

        self.setLayout(self.hbox)

    def set_css(self):
        self.setStyleSheet(f"""
            CreateSave
            {{
                background: {BACKGROUND};
            }}
            QScrollArea
            {{
                background: {BACKGROUND_DARKER};
                padding-bottom:10px;
            }}
            QLabel
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE};
            }}
        """)
        self.scroll_area.setStyleSheet(f"""
            PPButton
            {{
                margin: 10px 10px 0;
            }}
        """)

    def _create_list_of_saves(self):
        self.saves = BaseMainService.get_saves()
        self.save_buttons = []
        for index, save in enumerate(self.saves):
            save_button = PPButton(self, "stroke")
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
            self.picture_adding.set_text_to_lbl("Picture is added")

    def _open_save(self, title):
        self.current_save_chosen.emit(title)
        self.close()

    def _create_save(self): #TODO: check if title is creatable, forbidden symbols
        if self.save_pp_value.get_value_from_le() == "" or self.save_pp_value.get_value_from_le() in self.saves:
            return
        if self.picture_path == "":
            return
        title = self.save_pp_value.get_value_from_le().strip()
        if not check_filename(title):
            return

        BaseMainService.create_new_save(title)
        PictureMainService.add_new_picture(self.picture_path)
        self._open_save(title)

