from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QCheckBox

from consts import *

class PPChecker (QCheckBox):

    def __init__(self, label_text: str):
        super().__init__()
        self.setText(label_text)
        self.setFixedHeight(30)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.set_css()

    def set_css(self):
        self.setStyleSheet(f"""
            PPChecker
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE};
            }}
            PPChecker::indicator
            {{
                border-radius:8px;
                width:18px;
                height:18px;
            }}
            PPChecker::indicator:checked
            {{
                background-color: {PRIMARY};
                border: 1px solid {BACKGROUND_LIGHTER};
            }}
            PPChecker::indicator:unchecked
            {{
                background-color: {DISABLED};
                border: 1px solid {BACKGROUND_LIGHTER};
            }}
        """)