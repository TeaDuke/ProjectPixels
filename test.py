from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimer
import sys

class PPStatusBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("PPStatusBar")
        self.setFixedSize(400, 30)

        self.lbl1 = QLabel("Testing scroll text // ", self)
        self.lbl2 = QLabel("Testing scroll text // ", self)

        self.lbl1.move(0, 0)
        self.lbl2.move(-self.lbl1.width(), 0)

        self.timer = QTimer()
        self.timer.timeout.connect(self._scroll)
        self.timer.start(20)

        self.setStyleSheet("""
            #PPStatusBar {
                background-color: darkblue;
                color: white;
                font-size: 16px;
            }

            QLabel {
                background-color: transparent;
            }
        """)

    def _scroll(self):
        for label in (self.lbl1, self.lbl2):
            label.move(label.x() + 1, label.y())

        if self.lbl1.x() > self.width():
            self.lbl1.move(self.lbl2.x() - self.lbl1.width(), 0)
        if self.lbl2.x() > self.width():
            self.lbl2.move(self.lbl1.x() - self.lbl2.width(), 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PPStatusBar()
    w.show()
    sys.exit(app.exec())