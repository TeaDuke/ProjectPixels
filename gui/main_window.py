from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QSizePolicy

from gui.pixels_info import PixelsInfo
from gui.task_list import TaskList


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # declare widgets
        self.pxinfo = PixelsInfo()
        self.tasklist = TaskList()

        self.vbox = QVBoxLayout(self)

        self._settings()

    def _settings(self):
        self.resize(600,600)

        self.vbox.addWidget(self.pxinfo)
        self.vbox.addWidget(self.tasklist)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.vbox)