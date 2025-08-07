from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QGridLayout

from consts import *
from gui.custom_widgets.pp_lineedit import PPLineEdit


class PPEnterValue (QWidget):

    def __init__(self):
        super().__init__()

        self.lbl = QLabel()
        self.pp_le = PPLineEdit()
        self.grid = QGridLayout()

        self._settings()
        self.setCss()

    def _settings(self):

        self.lbl.setText("Something")
        self.lbl.setMinimumWidth(200)

        self.grid.addWidget(self.lbl, 0, 0)
        self.grid.addWidget(self.pp_le, 0, 1)

        self.setLayout(self.grid)

    def setCss(self):
        self.setStyleSheet(f"""
            QLabel
            {{
                color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
                font-size: {TEXT_SIZE}
            }}
        """)

    def setTextToLbl(self, text: str):
        self.lbl.setText(text)

    def getValueFromLE(self):
        return self.pp_le.text()