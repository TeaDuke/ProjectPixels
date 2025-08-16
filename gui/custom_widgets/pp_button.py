from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtWidgets import QPushButton, QSizePolicy

import consts
from consts import *
from enums.mode_enum import ModeEnum


class PPButton (QPushButton):

    btn_type = "default"
    badge = False
    badge_number = None
    parent = None
    task = None


    def __init__(self, parent, btn_type: str = "default"):
        super().__init__()
        self.parent = parent
        self.btn_type = btn_type.lower()
        self.set_css()

    def set_css(self):
        if self.btn_type == "default":
            self.setStyleSheet(f"""
                PPButton
                {{
                    color: {TEXT};
                    font-size: {TEXT_SIZE};
                    background-color: {PRIMARY};
                    border-radius: 8px;
                    padding: 6px 10px 6px 10px;
                    text-align: left;
                    border: 1px solid {PRIMARY};
                }}
                PPButton:hover
                {{
                    background-color: {SECONDARY};
                    border: 1px solid {SECONDARY};
                }}
                PPButton:disabled
                {{
                    background-color: {DISABLED};
                    border: 1px solid {DISABLED};
                    color: rgba({TEXT_DARKER_R}, {TEXT_DARKER_G}, {TEXT_DARKER_B}, {TEXT_DARKER_A});
                }}
            """)
        else:
            self.setStyleSheet(f"""
                PPButton
                {{
                    color: {TEXT};
                    font-size: {TEXT_SIZE};
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

    def mousePressEvent(self, event):
        if self.badge == True and self.parent.mode == ModeEnum.GENERAL:
            if event.button() == Qt.MouseButton.LeftButton:
                if self.badge_number is None:
                    number = 1
                else:
                    number = self.badge_number + 1
                self.set_badge_number(number)
            elif event.button() == Qt.MouseButton.RightButton:
                if self.badge_number is None:
                    number = None
                elif self.badge_number == 1:
                    number = None
                else:
                    number = self.badge_number - 1
                self.set_badge_number(number)

        super().mousePressEvent(event)

    def set_badge_functionality(self, badge: bool, task = None):
        self.badge = badge
        self.task = task

    def set_badge_number(self, number):
        self.badge_number = number
        self.update()  # Trigger repaint

    def get_badge_number(self):
        return self.badge_number

    def clear_badge_number(self):
        self.badge_number = None
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        if self.badge == True and self.badge_number is not None:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            # Badge circle size and position
            badge_radius = 12
            x = self.width() - badge_radius * 2 - badge_radius // 2
            y = badge_radius // 2

            # Draw red circle
            if self.btn_type == "default":
                painter.setBrush(QColor(consts.BACKGROUND))
            else:
                painter.setBrush(QColor(consts.PRIMARY))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, badge_radius * 2, badge_radius * 2)

            # Draw number
            painter.setPen(QColor(consts.TEXT))
            font = QFont()
            font.setPointSize(10)
            painter.setFont(font)

            # Center text in circle
            rect = QRect(x, y, badge_radius * 2, badge_radius * 2)
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(self.badge_number))
