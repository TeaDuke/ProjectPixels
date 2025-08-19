from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QLabel, QComboBox

from consts import TEXT, TEXT_SIZE
from data_services.save_data_service import SaveDataService
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_dropdown import PPDropDown
from services.save_main_service import SaveMainService


class Settings(QWidget):
    
    def __init__(self):
        super().__init__()

        self.opening_mode_lbl = QLabel()
        self.opening_mode_dd = PPDropDown()

        self.save_btn = PPButton(self, "default")
        self.cancel_btn = PPButton(self, "stroke")

        self.grid = QGridLayout()

        self.hbox_buttons = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.settings()
        self.set_css()
        self.update_settings()

    def settings(self):

        self.opening_mode_lbl.setText("Opening mode:")
        self.opening_mode_dd.set_items(["line", "random"])

        self.save_btn.setText("Save")
        self.save_btn.clicked.connect(self.save)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.grid.setContentsMargins(0,0,0,0)
        self.grid.addWidget(self.opening_mode_lbl, 0, 0)
        self.grid.addWidget(self.opening_mode_dd, 0, 1)

        self.hbox_buttons.setSpacing(20)
        self.hbox_buttons.addWidget(self.save_btn)
        self.hbox_buttons.addWidget(self.cancel_btn)

        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vbox.setContentsMargins(10,10,10,10)
        self.vbox.setSpacing(20)
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox_buttons)

        self.setLayout(self.vbox)

    def set_css(self):
        self.setStyleSheet(f"""
            QLabel
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE};
            }}
        """)

    def update_settings(self):
        op_mode = SaveMainService.get_opening_mode()
        self.opening_mode_dd.set_current_text(op_mode)

    def save(self):
        SaveMainService.update_opening_mode(self.opening_mode_dd.get_current_text())
        self.update_settings()
        self.close()