from PyQt6.QtWidgets import QPushButton

from colors import *


class PPButton (QPushButton):

    def __init__(self, btn_type: str = "default"):
        super().__init__()
        self.setCss(btn_type)

    def setCss(self, btn_type: str):
        if btn_type.lower() == "default":
            self.setStyleSheet(f"""
                PPButton
                {{
                    color: {TEXT};
                    font-size: 18px;
                    background-color: {PRIMARY};
                    border-radius: 8px;
                    padding: 6px 10px 6px 10px;
                    text-align: left;
                }}
                PPButton:hover
                {{
                    background-color: {SECONDARY};
                }}
                PPButton:disabled
                {{
                    background-color: {DISABLED};
                    color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
                }}
            """)
        else:
            self.setStyleSheet(f"""
                PPButton
                {{
                    color: {TEXT};
                    font-size: 18px;
                    background-color: {BACKGROUND};
                    border-radius: 8px;
                    padding: 6px 10px 6px 10px;
                    text-align: left;
                    border: 1px solid {PRIMARY};
                }}
                PPButton:hover
                {{
                    background-color: {BACKGROUND_LIGHTER};
                    border: 1px solid {SECONDARY};
                }}
                PPButton:disabled
                {{
                    background-color: {BACKGROUND};
                    border: 1px solid {DISABLED};
                    color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
                }}
            """)