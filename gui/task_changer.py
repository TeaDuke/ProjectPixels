from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox

from data_classes.Task import Task
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_enter_value import PPEnterValue
from services.task_main_service import TaskMainService


class TaskChanger(QWidget):
    task_updated = pyqtSignal()
    task_deleted = pyqtSignal(int)

    task = None

    def __init__(self):
        super().__init__()

        self.name_pp_value = PPEnterValue()
        self.price_pp_value = PPEnterValue()

        self.delete_btn = PPButton(self, "default")
        self.update_btn = PPButton(self, "default")
        self.cancel_btn = PPButton(self, "stroke")

        self.grid = QGridLayout()

        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.setWindowTitle("Change task")

        self.name_pp_value.set_text_to_lbl("Name:")
        self.price_pp_value.set_text_to_lbl("Price (in pixels):")

        self.delete_btn.setText("Delete")
        self.delete_btn.clicked.connect(self._delete_task)
        self.update_btn.setText("Update")
        self.update_btn.clicked.connect(self._update_task)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.hbox.setContentsMargins(10, 10, 10, 0)
        self.hbox.setSpacing(10)
        self.hbox.addWidget(self.delete_btn)
        self.hbox.addWidget(self.update_btn)
        self.hbox.addWidget(self.cancel_btn)

        self.vbox.addWidget(self.name_pp_value)
        self.vbox.addWidget(self.price_pp_value)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def set_task(self, task: Task):
        self.task = task
        self.name_pp_value.set_text_to_le(self.task.name)
        self.price_pp_value.set_text_to_le(str(self.task.price))

    def _delete_task(self):
        reply = QMessageBox.question(self, "Delete task", "Are you sure?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            TaskMainService.delete_task(self.task)
            self.task_deleted.emit(self.task.tid)
            self.close()

    def _update_task(self):
        if not self._validation_check():
            return
        self.task.update_name(self.name_pp_value.get_value_from_le())
        self.task.update_price(int(self.price_pp_value.get_value_from_le()))
        TaskMainService.update_task(self.task)
        self.task_updated.emit()
        self.close()

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
