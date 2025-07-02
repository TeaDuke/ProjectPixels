from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel


class StatusLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text = "", color = "",  parent = None):
        super().__init__(text=text, parent=parent)
        self.color = str(color).lower()
        self._settings()

    def _settings(self):
        if self.color == "velvet":
            self.setStyleSheet("background-color: SlateBlue; color: white")
        elif self.color == "red":
            self.setStyleSheet("background-color: Tomato; color: white")
        elif self.color == "green":
            self.setStyleSheet("background-color: MediumSeaGreen; color: white")

    def setStatusColor(self, color):
        self.color = str(color).lower()
        self._settings()

    def mousePressEvent(self, ev):
        self.clicked.emit()