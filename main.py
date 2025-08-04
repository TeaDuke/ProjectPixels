import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from gui.main_window import MainWindow
from gui.start_up import StartUp


def start():

    app = QApplication(sys.argv)
    # app.setStyle()
    start_up = StartUp()
    app.exec()

if __name__ == '__main__':
    start()

