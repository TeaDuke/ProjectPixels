from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_click)  # ✅ Correct usage
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        print("Button clicked!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
