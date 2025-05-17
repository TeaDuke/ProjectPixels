from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QLabel, QComboBox

from data_services.save_data_service import SaveDataService
from services.save_main_service import SaveMainService


class Settings(QWidget):
    
    def __init__(self):
        super().__init__()

        self.opening_mode_lbl = QLabel()
        self.opening_mode_combo = QComboBox()

        self.save_btn = QPushButton()
        self.cancel_btn = QPushButton()

        self.grid = QGridLayout()

        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.settings()

    def settings(self):

        self.opening_mode_lbl.setText("Opening mode:")
        self.opening_mode_combo.addItems(["line", "random"])

        self.grid.addWidget(self.opening_mode_lbl, 0, 0)
        self.grid.addWidget(self.opening_mode_combo, 0, 1)

        self.save_btn.setText("Save")
        self.save_btn.clicked.connect(self.save)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.hbox.addWidget(self.save_btn)
        self.hbox.addWidget(self.cancel_btn)

        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def update_settings(self):
        op_mode = SaveMainService.get_opening_mode()
        self.opening_mode_combo.setCurrentText(op_mode)

    def save(self):
        SaveMainService.update_opening_mode(self.opening_mode_combo.currentText())
        self.update_settings()