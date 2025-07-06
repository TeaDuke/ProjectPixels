from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox

from data_classes.Task import Task
from services.task_main_service import TaskMainService


class TaskChanger(QWidget):
    task_updated = pyqtSignal()
    task_deleted = pyqtSignal(int)

    task = None

    def __init__(self):
        super().__init__()

        self.title_lbl = QLabel()

        self.name_info_lbl = QLabel()
        self.name_value_le = QLineEdit()
        self.price_info_lbl = QLabel()
        self.price_value_le = QLineEdit()

        self.delete_btn = QPushButton()
        self.update_btn = QPushButton()
        self.cancel_btn = QPushButton()

        self.grid = QGridLayout()

        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.title_lbl.setText("Change task")

        self.name_info_lbl.setText("Name:")
        self.price_info_lbl.setText("Price (in pixels):")

        self.delete_btn.setText("Delete")
        self.delete_btn.clicked.connect(self._delete_task)
        self.update_btn.setText("Update")
        self.update_btn.clicked.connect(self._update_task)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.grid.addWidget(self.name_info_lbl, 0, 0)
        self.grid.addWidget(self.name_value_le, 0, 1)
        self.grid.addWidget(self.price_info_lbl, 1, 0)
        self.grid.addWidget(self.price_value_le, 1, 1)

        self.hbox.addWidget(self.delete_btn)
        self.hbox.addWidget(self.update_btn)
        self.hbox.addWidget(self.cancel_btn)

        self.vbox.addWidget(self.title_lbl)
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def set_task(self, task: Task):
        self.task = task
        self.name_value_le.setText(self.task.name)
        self.price_value_le.setText(str(self.task.price))

    def _delete_task(self):
        reply = QMessageBox.question(self, "Delete task", "Are you sure?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            TaskMainService.delete_task(self.task)
            self.task_deleted.emit(self.task.tid)
            self.close()

    def _update_task(self):
        self.task.update_name(self.name_value_le.text())
        self.task.update_price(int(self.price_value_le.text()))
        TaskMainService.update_task(self.task)
        self.task_updated.emit()
        self.close()

    def closeEvent(self, event):
        self.name_value_le.clear()
        self.price_value_le.clear()
        event.accept()
