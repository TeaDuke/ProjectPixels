from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt

from gui.task_creator import TaskCreator
from utilits.palette_utilit import get_palette

listBtn = ["work-out", "read", "pray", "no sugar", "japan"]

class TaskList(QWidget):

    def __init__(self):
        super().__init__()
        self.container = QWidget()

        self.add_btn = QPushButton()

        self.task_creator = TaskCreator()

        self.hbox = QHBoxLayout()
        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self._settings()

    def _settings(self):
        self.resize(300, 200)
        self.setAutoFillBackground(True)
        self.setPalette(get_palette(217,217,217))

        self.add_btn.setText("Add XXXX")
        self.add_btn.clicked.connect(self.open_task_creator)

        self.hbox.addWidget(self.add_btn)
        self.hbox.setAlignment(Qt.AlignmentFlag.AlignRight)

        self._create_buttons()

        widget = QWidget()
        widget.setLayout(self.grid)
        widget.setAutoFillBackground(True)
        widget.setPalette(get_palette(212, 44, 44))

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(widget)

        self.setLayout(self.vbox)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def _create_buttons(self):
        place = 0
        for btn in listBtn:
            qbtn = QPushButton(btn)
            self.grid.addWidget(qbtn, place//2, place%2)
            place += 1

    def open_task_creator(self):
        self.task_creator.show()