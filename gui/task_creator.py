from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QHBoxLayout, QPushButton

from data_classes.Task import Task
from services.task_main_service import TaskMainService


class TaskCreator(QWidget):
    task_created = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.title_lbl = QLabel()

        self.name_info_lbl = QLabel()
        self.name_value_le = QLineEdit()
        self.price_info_lbl = QLabel()
        self.price_value_le = QLineEdit()

        self.create_btn = QPushButton()
        self.cancel_btn = QPushButton()

        self.grid = QGridLayout()

        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.title_lbl.setText("Create task")

        self.name_info_lbl.setText("Name:")
        self.price_info_lbl.setText("Price (in pixels):")

        self.create_btn.setText("Create")
        self.create_btn.clicked.connect(self._add_task)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.grid.addWidget(self.name_info_lbl, 0, 0)
        self.grid.addWidget(self.name_value_le, 0, 1)
        self.grid.addWidget(self.price_info_lbl, 1, 0)
        self.grid.addWidget(self.price_value_le, 1, 1)

        self.hbox.addWidget(self.create_btn)
        self.hbox.addWidget(self.cancel_btn)

        self.vbox.addWidget(self.title_lbl)
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def _add_task(self):
        if not self._validation_check():
            return
        new_tid = TaskMainService.get_new_tid()
        task = Task(new_tid ,self.name_value_le.text(), self.price_value_le.text())
        TaskMainService.add_task(task)
        self.task_created.emit()

    def _validation_check(self):
        if self.name_value_le.text() == "" or self.price_value_le.text() == "":
            return False
        try:
            price = int(self.price_value_le.text())
            return True
        except Exception as e:
            print(f"Price is not number. Exception: {e}")
            return False

    def closeEvent(self, event):
        self.name_value_le.clear()
        self.price_value_le.clear()
        event.accept()
