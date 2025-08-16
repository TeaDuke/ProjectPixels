from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QHBoxLayout, QPushButton

from data_classes.Task import Task
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_enter_value import PPEnterValue
from services.task_main_service import TaskMainService


class TaskCreator(QWidget):
    task_created = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.name_pp_value = PPEnterValue()
        self.price_pp_value = PPEnterValue()

        self.create_btn = PPButton(self, "default")
        self.cancel_btn = PPButton(self, "stroke")

        self.grid = QGridLayout()

        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.setWindowTitle("Create task")

        self.name_pp_value.set_text_to_lbl("Name:")
        self.price_pp_value.set_text_to_lbl("Price (in pixels):")

        self.create_btn.setText("Create")
        self.create_btn.clicked.connect(self._add_task)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.hbox.setContentsMargins(10, 10, 10, 0)
        self.hbox.setSpacing(10)
        self.hbox.addWidget(self.create_btn)
        self.hbox.addWidget(self.cancel_btn)

        self.vbox.addWidget(self.name_pp_value)
        self.vbox.addWidget(self.price_pp_value)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def _add_task(self):
        if not self._validation_check():
            return
        new_tid = TaskMainService.get_new_tid()
        task = Task(new_tid, self.name_pp_value.get_value_from_le(), self.price_pp_value.get_value_from_le())
        TaskMainService.add_task(task)
        self.task_created.emit()

    def _validation_check(self):
        if self.name_pp_value.get_value_from_le() == "" or self.price_pp_value.get_value_from_le() == "":
            return False
        try:
            price = int(self.price_pp_value.get_value_from_le())
            return True
        except Exception as e:
            print(f"Price is not number. Exception: {e}")
            return False

    def closeEvent(self, event):
        self.name_pp_value.set_text_to_le("")
        self.price_pp_value.set_text_to_le("")
        event.accept()
