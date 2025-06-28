from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal

from data_classes.Task import Task
from gui.custom_widgets.badge_button import BadgeButton
from gui.task_creator import TaskCreator
from services.picture_main_service import PictureMainService
from services.task_main_service import TaskMainService
from utilits.palette_utilit import get_palette


class TaskList(QWidget):
    tasks = []
    place = 0
    buttons = []

    mode =

    tasks_saved = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.finished_tasks = {}

        self.container = QWidget()

        self.save_btn = QPushButton()
        self.change_btn = QPushButton()
        self.add_btn = QPushButton()

        self.task_creator = TaskCreator()
        self.task_creator.task_created.connect(self._create_buttons)

        self.hbox = QHBoxLayout()
        self.grid = QGridLayout()
        self.vbox = QVBoxLayout()
        self._settings()

    def _settings(self):
        self.resize(300, 200)
        self.setAutoFillBackground(True)
        self.setPalette(get_palette(217,217,217))

        self.save_btn.setText("Save tasks")
        self.save_btn.clicked.connect(self.save_tasks)
        self.change_btn.setText("Change: Off")
        self.change_btn.clicked.connect(self.change_tasks)
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
        self.tasks = TaskMainService.getTasks()
        st = self.place
        for i in range(st, len(self.tasks)):
            self.buttons.append(BadgeButton(f"{self.tasks[i].name}"))
            self.buttons[self.place].clicked.connect(self.finish_task)
            self.grid.addWidget(self.buttons[self.place], self.place // 2, self.place % 2)
            self.place += 1
        self.grid.update()

    def open_task_creator(self):
        self.task_creator.show()

    def finish_task(self):
        name = self.sender().text()
        if name not in self.finished_tasks:
            self.finished_tasks[name] = 0
        self.finished_tasks[name] += 1

    def _find_task_index_by_name(self, name):
        return self.tasks.index(Task(name, 0))

    def save_tasks(self):
        number = 0
        for name in self.finished_tasks:
            index = self._find_task_index_by_name(name)
            number += self.tasks[index].price * self.finished_tasks[name]
            self.buttons[index].clear_badge_number()
        # self.save_btn.setText(str(number))
        self.finished_tasks = {}
        if number != 0:
            PictureMainService.open_pixels(number)
            self.tasks_saved.emit()

    def change_tasks(self):
