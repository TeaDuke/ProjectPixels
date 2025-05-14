from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import QRect, Qt

class BadgeButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.badge_number = None  # No badge initially

    def mousePressEvent(self, event):
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

    def set_badge_number(self, number):
        self.badge_number = number
        self.update()  # Trigger repaint

    def clear_badge_number(self):
        self.badge_number = None
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        if self.badge_number is not None:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            # Badge circle size and position
            badge_radius = 8
            x = self.width() - badge_radius * 2
            y = 0

            # Draw red circle
            painter.setBrush(QColor("white"))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, badge_radius * 2, badge_radius * 2)

            # Draw number
            painter.setPen(QColor("black"))
            font = QFont()
            font.setBold(True)
            font.setPointSize(8)
            painter.setFont(font)

            # Center text in circle
            rect = QRect(x, y, badge_radius * 2, badge_radius * 2)
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(self.badge_number))