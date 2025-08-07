from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton

from utilits.image_utilits import resource_path

from consts import *

class PPIconButton(QPushButton):

    btn_type = "default"
    icon_type = "left"

    def __init__(self, btn_type: str = "default", icon_type: str = "left"):
        super().__init__()
        self.btn_type = btn_type.lower()
        self.icon_type = icon_type.lower()
        self._updateIcon()
        self.setCss()

    def setCss(self):
        if self.btn_type == "default":
            self.setStyleSheet(f"""
                PPIconButton
                {{
                    color: {TEXT};
                    font-size: {TEXT_SIZE};
                    background-color: {PRIMARY};
                    border-radius: 8px;
                    padding: 6px;
                    text-align: left;
                }}
                PPIconButton:hover
                {{
                    background-color: {SECONDARY};
                }}
                PPIconButton:disabled
                {{
                    background-color: {DISABLED};
                    color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
                }}
            """)
        else:
            self.setStyleSheet(f"""
                PPIconButton
                {{
                    color: {TEXT};
                    font-size: {TEXT_SIZE};
                    background-color: {BACKGROUND};
                    border-radius: 8px;
                    padding: 6px;
                    text-align: left;
                    border: 1px solid {PRIMARY};
                }}
                PPIconButton:hover
                {{
                    background-color: {BACKGROUND_LIGHTER};
                    border: 1px solid {SECONDARY};
                }}
                PPIconButton:disabled
                {{
                    background-color: {BACKGROUND};
                    border: 1px solid {DISABLED};
                    color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
                }}
            """)

    def setIconType(self, icon_type: str = "left"):
        self.icon_type = icon_type.lower()
        self._updateIcon()

    def _updateIcon(self):
        if self.icon_type == "left":
            self.setIcon(QIcon(resource_path("chevron-left.svg")))
        elif self.icon_type == "right":
            self.setIcon(QIcon(resource_path("chevron-right.svg")))
        elif self.icon_type == "delete":
            self.setIcon(QIcon(resource_path("trash.svg")))
        elif self.icon_type == "settings":
            self.setIcon(QIcon(resource_path("cog.svg")))
        self.setIconSize(QSize(24,24))

