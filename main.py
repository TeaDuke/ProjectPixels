import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from gui.main_window import MainWindow


def start():
    app = QApplication(sys.argv)
    # app.setStyle()
    window = QMainWindow()
    window.setCentralWidget(MainWindow())
    window.resize(600,600)
    window.show()
    app.exec()

if __name__ == '__main__':
    start()

