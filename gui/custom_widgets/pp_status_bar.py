from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QSizePolicy

from consts import *
from enums.status_enum import StatusEnum


class PPStatusBar (QWidget):

    parent = None
    mode = StatusEnum.IN_PROGRESS
    speed = 1

    def __init__(self, parent, mode: StatusEnum):
        super().__init__()
        self.setFixedHeight(30)
        self.setFixedWidth(parent.width())
        self.parent = parent
        self.mode = mode

        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)

        self.timer = QTimer(self)

        self._settings()
        self.set_css()

    def _settings(self):
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.lbl1.setFixedHeight(30)
        self.lbl1.move(self.width(), 0)
        self.lbl2.setFixedHeight(30)
        self.lbl2.move(self.width(), 0)

        if self.mode == StatusEnum.IN_PROGRESS:
            self.lbl1.setText(
                "IN PROGRESS // in progress // IN PROGRESS // in progress // IN PROGRESS // in progress // IN PROGRESS // in progress // ")
            self.lbl2.setText(
                "IN PROGRESS // in progress // IN PROGRESS // in progress // IN PROGRESS // in progress // IN PROGRESS // in progress // ")
        elif self.mode == StatusEnum.STOPPED:
            self.lbl1.setText(
                "STOPPED // stopped // STOPPED // stopped // STOPPED // stopped // STOPPED // stopped // STOPPED // stopped // ")
            self.lbl2.setText(
                "STOPPED // stopped // STOPPED // stopped // STOPPED // stopped // STOPPED // stopped // STOPPED // stopped // ")
        else:
            self.lbl1.setText(
                "FINISHED // finished // FINISHED // finished // FINISHED // finished // FINISHED // finished // FINISHED // finished // ")
            self.lbl2.setText(
                "FINISHED // finished // FINISHED // finished // FINISHED // finished // FINISHED // finished // FINISHED // finished // ")

        self.timer.timeout.connect(self._scroll)
        self.timer.start(20)


    def set_css(self):
        background_color = ""

        if self.mode == StatusEnum.IN_PROGRESS:
            background_color = PRIMARY
        elif self.mode == StatusEnum.STOPPED:
            background_color = STOPPED
        else:
            background_color = FINISHED

        self.setStyleSheet(f"""
            QLabel
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE_2};
                font-weight: bold;
            }}
            PPStatusBar 
            {{
                background-color: {background_color};
            }}
        """)

    def _scroll(self):
        for label in (self.lbl1, self.lbl2):
            label.move(label.x() + self.speed, label.y())

        if self.lbl1.x() > self.width():
            self.lbl1.move(self.lbl2.x() - self.lbl1.width(), 0)
        if self.lbl2.x() > self.width():
            self.lbl2.move(self.lbl1.x() - self.lbl2.width(), 0)

