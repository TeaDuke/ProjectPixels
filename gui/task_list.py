from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal

from data_classes.Task import Task
from enums.mode_enum import ModeEnum
from gui.custom_widgets.badge_button import BadgeButton
from gui.task_changer import TaskChanger
from gui.task_creator import TaskCreator
from services.picture_main_service import PictureMainService
from services.task_main_service import TaskMainService
from utilits.layout_utilit import clear_layout
from utilits.palette_utilit import get_palette


class TaskList(QWidget):
    tasks = []
    place = 0
    buttons = []

    mode = ModeEnum.GENERAL

    tasks_saved = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.container = QWidget()

        self.save_btn = QPushButton()
        self.change_btn = QPushButton()
        self.add_btn = QPushButton()

        self.task_creator = TaskCreator()
        self.task_creator.task_created.connect(self.add_task)

        self.task_changer = TaskChanger()
        self.task_changer.task_updated.connect(self.update_task)
        self.task_changer.task_deleted.connect(self.delete_task)

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
        self.change_btn.clicked.connect(self.change_mode)
        self.add_btn.setText("Add XXXX")
        self.add_btn.clicked.connect(self.open_task_creator)

        self.hbox.addWidget(self.save_btn)
        self.hbox.addWidget(self.change_btn)
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

        finished_tasks = {}
        for button in self.buttons:
            finished_tasks[button.task.tid] = button.get_badge_number()

        self.buttons.clear()
        clear_layout(self.grid)
        for i in range(0, len(self.tasks)):
            self.buttons.append(BadgeButton(f"{self.tasks[i].name}", self.tasks[i], self))
            if self.tasks[i].tid in finished_tasks.keys():
                self.buttons[i].set_badge_number(finished_tasks[self.tasks[i].tid])
            self.buttons[i].clicked.connect(self.button_buffer)
            self.grid.addWidget(self.buttons[i], i // 2, i % 2)
        self.grid.update()

    def open_task_creator(self):
        self.task_creator.show()

    def open_task_changer(self, task: Task):
        self.task_changer.set_task(task)
        self.task_changer.show()

    def add_task(self):
        self._create_buttons()

    def update_task(self):
        self._create_buttons()

    def delete_task(self, tid):
        self._create_buttons()

    def button_buffer(self):
        if self.mode == ModeEnum.GENERAL:
            pass
        elif self.mode == ModeEnum.CHANGE:
            self.open_task_changer(self.sender().task)

    def _find_task_index_by_tid(self, tid):
        return self.tasks.index(Task(tid, "", 0))

    def save_tasks(self):
        number = 0
        for button in self.buttons:
            if button.get_badge_number() is not None:
                number += button.task.price * button.get_badge_number()
            button.clear_badge_number()
        if number != 0:
            PictureMainService.open_pixels(number)
            self.tasks_saved.emit()

    def change_mode(self):
        if self.mode == ModeEnum.GENERAL:
            self.mode = ModeEnum.CHANGE
            self.change_btn.setStyleSheet("background-color: red")
            self.change_btn.setText("Change: On")
        elif self.mode == ModeEnum.CHANGE:
            self.mode = ModeEnum.GENERAL
            self.change_btn.setStyleSheet("")
            self.change_btn.setText("Change: Off")