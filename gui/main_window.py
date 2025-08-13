from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPalette, QColor, QIcon
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QSizePolicy, QTabBar, QPushButton, QComboBox

from consts import BACKGROUND
from enums.status_enum import StatusEnum
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_checker import PPChecker
from gui.custom_widgets.pp_dropdown import PPDropDown
from gui.custom_widgets.pp_entervalue import PPEnterValue
from gui.custom_widgets.pp_iconbutton import PPIconButton
from gui.custom_widgets.pp_info import PPInfo
from gui.custom_widgets.pp_lineedit import PPLineEdit
from gui.custom_widgets.pp_statusbar import PPStatusBar
from gui.pixels_info import PixelsInfo
from gui.settings import Settings
from gui.task_list import TaskList
from services.base_main_service import BaseMainService
from utilits.image_utilits import resource_path


class MainWindow(QWidget):

    current_save_changed = pyqtSignal(str)
    open_create_save = pyqtSignal()

    saves = []
    current_save = ""

    def __init__(self):
        super().__init__()

        # declare widgets
        self.tabbar = QTabBar()

        self.pp_btn = PPButton(self, "default")
        self.pp_le = PPLineEdit()
        self.pp_ev = PPEnterValue()
        self.pp_dd = PPDropDown()
        self.pp_info = PPInfo()
        self.pp_icon_btn = PPIconButton("stroke", "left")
        self.pp_status_bar = PPStatusBar(self, StatusEnum.FINISHED)
        self.pp_checker = PPChecker("Change mode")

        self.settings_window = Settings()

        self.saves_combo = QComboBox()
        self.new_save_btn = QPushButton()

        self.pxinfo = PixelsInfo()
        self.tasklist = TaskList()

        self.vbox = QVBoxLayout()

        self._settings()
        self.setCss()

    def _settings(self):
        self.resize(600,600)

        self.saves = BaseMainService.get_saves()
        self.current_save = BaseMainService.get_current_save()

        self.tabbar.addTab("Settings")
        self.tabbar.tabBarClicked.connect(self.tab_clicked)

        self.saves_combo.addItems(self.saves)
        self.saves_combo.setCurrentText(self.current_save)
        self.saves_combo.currentTextChanged.connect(lambda: self._change_current_save(self.saves_combo.currentText()))

        self.pp_btn.setText("PP button")
        self.pp_ev.setTextToLbl("Task name:")
        self.pp_dd.setMaximumWidth(200)
        self.pp_dd.setItems(self.saves)
        self.pp_dd.setCurrentText(self.current_save)

        self.new_save_btn.setText("Create new Save")
        self.new_save_btn.clicked.connect(self._open_create_save)

        self.tasklist.tasks_saved.connect(self.update_pixels_info)

        self.vbox.addWidget(self.tabbar)
        self.vbox.addWidget(self.saves_combo)

        self.vbox.addWidget(self.pp_btn)
        self.vbox.addWidget(self.pp_le)
        self.vbox.addWidget(self.pp_ev)
        self.vbox.addWidget(self.pp_dd)
        self.vbox.addWidget(self.pp_info)
        self.vbox.addWidget(self.pp_icon_btn)
        self.vbox.addWidget(self.pp_status_bar)
        self.vbox.addWidget(self.pp_checker)

        self.vbox.addWidget(self.new_save_btn)
        self.vbox.addWidget(self.pxinfo)
        self.vbox.addWidget(self.tasklist)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.vbox)

    def setCss(self):
        self.setStyleSheet(f"""
            MainWindow
            {{
                background-color: {BACKGROUND};
            }}
        """)

    def update_pixels_info(self):
        self.pxinfo.update_pixels_info()

    def tab_clicked(self, index):
        self.settings_window.update_settings()
        self.settings_window.show()

    def _change_current_save(self, title):
        self.current_save_changed.emit(title)
        self.settings_window.close()
        self.tasklist.close_windows()
        self.pxinfo.close_windows()
        self.close()

    def _open_create_save(self):
        self.open_create_save.emit()
        self.settings_window.close()
        self.tasklist.close_windows()
        self.pxinfo.close_windows()
        self.close()