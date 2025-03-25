import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

from classes.imagepp import ImagePP
from classes.main_interface import MainInterface
from classes.save import Save


class MainWindow(QMainWindow):



    img = ImagePP

    def __init__(self):
        super().__init__()

        Save.read_save()

        self.m_interface = MainInterface()
        self.m_interface.resize(600, 600)
        print("after resize")
        self.setCentralWidget(self.m_interface)
        # fileName = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        # print(fileName)
        # img = ImagePP(id="27")
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()