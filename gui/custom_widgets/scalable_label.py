from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QLabel


class ScalableLabel(QLabel):
    def sizeHint(self):
        return QSize(100, 100)

    def minimumSizeHint(self):
        return QSize(0, 0)