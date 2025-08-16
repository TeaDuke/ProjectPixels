from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from consts import *


class PPInfo (QWidget):

    def __init__(self):
        super().__init__()

        self.label_lbl = QLabel()
        self.value_lbl = QLabel()

        self.vbox = QVBoxLayout()

        self._settings()
        self.set_css()

    def _settings(self):
        self.label_lbl.setText("Something")
        self.value_lbl.setText("1234")

        self.vbox.setContentsMargins(0,0,0,0)
        self.vbox.addWidget(self.label_lbl)
        self.vbox.addWidget(self.value_lbl)

        self.setLayout(self.vbox)

    def set_css(self):
        self.label_lbl.setStyleSheet(f"""
            QLabel
            {{
                font-size: {TEXT_SIZE};
                color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
            }}
        """)
        self.value_lbl.setStyleSheet(f"""
            QLabel
            {{
                font-size: {TEXT_SIZE_2};
                color: {TEXT};
            }}
        """)

    def set_label(self, text:str):
        self.label_lbl.setText(text)

    def set_value(self, text:str):
        self.value_lbl.setText(text)