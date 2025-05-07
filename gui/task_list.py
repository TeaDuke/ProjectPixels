from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt

from gui.task_creator import TaskCreator
from services.task_main_service import TaskMainService
from utilits.palette_utilit import get_palette
from utilits.layout_utilit import clear_layout

class TaskList(QWidget):
    place = 0

    def __init__(self):
        super().__init__()
        self.container = QWidget(self)

        self.save_btn = QPushButton(self)
        self.add_btn = QPushButton(self)

        self.task_creator = TaskCreator()
        self.task_creator.task_created.connect(self._create_buttons)

        self.hbox = QHBoxLayout(self)
        self.grid = QGridLayout(self)
        self.vbox = QVBoxLayout(self)
        self._settings()

    def _settings(self):
        self.resize(300, 200)
        self.setAutoFillBackground(True)
        self.setPalette(get_palette(217,217,217))

        self.save_btn.setText("Save tasks")
        self.add_btn.setText("Add XXXX")
        self.add_btn.clicked.connect(self.open_task_creator)

        self.hbox.addWidget(self.save_btn)
        self.hbox.addWidget(self.add_btn)

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
        tasks = TaskMainService.getTasks()
        st = self.place
        for i in range(st, len(tasks)):
            qbtn = QPushButton(f"{tasks[i].name} ({tasks[i].price})")
            self.grid.addWidget(qbtn, self.place // 2, self.place % 2)
            self.place += 1
        self.grid.update()

    def open_task_creator(self):
        self.task_creator.show()