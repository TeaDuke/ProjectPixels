from PyQt6.QtWidgets import QLineEdit

from colors import *


class PPLineEdit (QLineEdit):

    def __init__(self):
        super().__init__()
        self.setCss()

    def setCss(self):
        self.setStyleSheet(f"""
            PPLineEdit
            {{
                color: {TEXT};
                font-size: 18px;
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