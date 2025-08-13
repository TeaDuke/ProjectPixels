from PyQt6.QtWidgets import QLineEdit

from consts import *


class PPLineEdit (QLineEdit):

    def __init__(self):
        super().__init__()
        self.setMinimumWidth(120)
        self.setCss()

    def setCss(self):
        self.setStyleSheet(f"""
            PPLineEdit
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE};
                background-color: {BACKGROUND_LIGHTER};
                border-radius: 8px;
                padding: 6px 10px 6px 10px;
                text-align: left;
                border: 1px solid {BACKGROUND_LIGHTER};
            }}
            PPLineEdit:focus
            {{
                border: 1px solid {PRIMARY}
            }}
        """)