from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QSizePolicy, QTabBar

from gui.pixels_info import PixelsInfo
from gui.settings import Settings
from gui.task_list import TaskList


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # declare widgets
        self.tabbar = QTabBar()

        self.settings_window = Settings()

        self.pxinfo = PixelsInfo()
        self.tasklist = TaskList()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.resize(600,600)

        self.tabbar.addTab("Settings")
        self.tabbar.tabBarClicked.connect(self.tab_clicked)

        self.tasklist.tasks_saved.connect(self.update_pixels_info)

        self.vbox.addWidget(self.tabbar)
        self.vbox.addWidget(self.pxinfo)
        self.vbox.addWidget(self.tasklist)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.vbox)

    def update_pixels_info(self):
        self.pxinfo.update_pixels_info()

    def tab_clicked(self, index):
        self.settings_window.update_settings()
        self.settings_window.show()