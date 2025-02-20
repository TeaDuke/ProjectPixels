import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

from classes.image import ImagePP


class MainWindow(QMainWindow):

    img = ImagePP

    def __init__(self):
        super().__init__()
        fileName = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        print(fileName[0])
        img = ImagePP(ipath=fileName[0])
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()