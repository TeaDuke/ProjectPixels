import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from classes.image import ImagePP


class MainWindow(QMainWindow):

    img = ImagePP

    def __init__(self):
        super().__init__()
        img = ImagePP(ipath="C:\\Users\\maxch\\Pictures\\изображение_2023-08-22_161429967.png")
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()