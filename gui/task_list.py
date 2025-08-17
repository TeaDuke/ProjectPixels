from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import pyqtSignal, Qt

from consts import BACKGROUND_DARKER
from data_classes.Task import Task
from enums.mode_enum import ModeEnum
from gui.custom_widgets.badge_button import BadgeButton
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_checker import PPChecker
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

    parent = None

    tasks_saved = pyqtSignal()


    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.container = QWidget()

        self.save_btn = PPButton(self, "default")
        self.create_btn = PPButton(self, "default")
        self.change_checker = PPChecker("Change mode")

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
        self.save_btn.setText("Save tasks")
        self.save_btn.clicked.connect(self.save_tasks)
        self.save_btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.create_btn.setText("Add task")
        self.create_btn.clicked.connect(self.open_task_creator)
        self.create_btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.change_checker.clicked.connect(self.change_mode)

        self.hbox.setSpacing(20)
        self.hbox.setContentsMargins(0,0,0,0)
        self.hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.hbox.addWidget(self.save_btn)
        self.hbox.addWidget(self.create_btn)
        self.hbox.addWidget(self.change_checker)

        self._create_buttons()

        self.grid.setSpacing(15)
        self.grid.setContentsMargins(10,15,10,15)
        widget = QWidget()
        widget.setMinimumWidth(self.parent.width()-40)
        widget.setLayout(self.grid)
        widget.setStyleSheet(f"""
            background: {BACKGROUND_DARKER};
            border-radius: 10px;
        """)

        self.vbox.setContentsMargins(0,0,0,0)
        self.vbox.setSpacing(20)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(widget)

        self.setLayout(self.vbox)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def _create_buttons(self):
        self.tasks = TaskMainService.get_tasks()

        finished_tasks = {}
        for button in self.buttons:
            finished_tasks[button.task.tid] = button.get_badge_number()

        self.buttons.clear()
        clear_layout(self.grid)
        for i in range(0, len(self.tasks)):
            pp_btn = PPButton(self, "stroke")
            pp_btn.set_badge_functionality(True, self.tasks[i])
            pp_btn.setText(f"{self.tasks[i].name}")
            self.buttons.append(pp_btn)
            if self.tasks[i].tid in finished_tasks.keys():
                self.buttons[i].set_badge_number(finished_tasks[self.tasks[i].tid])
            self.buttons[i].clicked.connect(self.button_buffer)
            self.grid.addWidget(self.buttons[i], i // 3, i % 3)
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
        elif self.mode == ModeEnum.CHANGE:
            self.mode = ModeEnum.GENERAL

    def close_windows(self):
        self.task_creator.close()
        self.task_changer.close()