from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QGridLayout

from consts import *
from gui.custom_widgets.pp_line_edit import PPLineEdit


class PPEnterValue (QWidget):

    def __init__(self):
        super().__init__()

        self.lbl = QLabel()
        self.pp_le = PPLineEdit()
        self.grid = QGridLayout()

        self._settings()
        self.set_css()

    def _settings(self):

        self.lbl.setText("Something")
        self.lbl.setMinimumWidth(200)

        self.grid.addWidget(self.lbl, 0, 0)
        self.grid.addWidget(self.pp_le, 0, 1)

        self.setLayout(self.grid)

    def set_css(self):
        self.setStyleSheet(f"""
            QLabel
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE}
            }}
        """)

    def set_text_to_lbl(self, text: str):
        self.lbl.setText(text)

    def set_text_to_le(self, text: str):
        self.pp_le.setText(text)

    def get_value_from_le(self):
        return self.pp_le.text()