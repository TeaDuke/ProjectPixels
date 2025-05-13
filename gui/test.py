from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys
from PyQt6.QtGui import QImage, QColor, QRgba64
from data_services.picture_data_service import PictureDataService
from services.picture_main_service import PictureMainService

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.button = QPushButton("Click Me")
#         self.button.clicked.connect(self.on_click)  # ✅ Correct usage
#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#
#     def on_click(self):
#         print("Button clicked!")
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

# with open(f"data\\base.json", 'r', encoding='utf-8') as f:
#     print(f)
#
# PictureMainService.open_pixels(10)

ppic = QImage()
print(ppic.height())
color = QColor(ppic.pixel(1, 1))
rgba = QRgba64()
rgba.setRed(color.red())
rgba.setGreen(color.green())
rgba.setBlue(color.blue())
rgba.setAlpha(0)


print(f"color: r - {color.red()}, g - {color.green()}, b - {color.blue()}, a - {color.alpha()},")
ppic.setPixel(1, 1, rgba.toArgb32())
ppic.save(f"data\\upd.png")