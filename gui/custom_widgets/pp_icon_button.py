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
        self._update_icon()
        self.set_css()

    def set_css(self):
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

    def set_icon_type(self, icon_type: str = "left"):
        self.icon_type = icon_type.lower()
        self._update_icon()

    def _update_icon(self):
        if self.icon_type == "left":
            self.setIcon(QIcon(resource_path("images\\chevron-left.svg")))
        elif self.icon_type == "right":
            self.setIcon(QIcon(resource_path("images\\chevron-right.svg")))
        elif self.icon_type == "delete":
            self.setIcon(QIcon(resource_path("images\\trash.svg")))
        elif self.icon_type == "settings":
            self.setIcon(QIcon(resource_path("images\\cog.svg")))
        self.setIconSize(QSize(24,24))

    def resizeEvent(self, event):
        size = min(event.size().width(), event.size().height())
        self.setFixedSize(size, size)
        super().resizeEvent(event)

