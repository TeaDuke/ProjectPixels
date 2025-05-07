from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout


class PictureInfo(QWidget):

    def __init__(self):
        super().__init__()

        self.picture = QLabel()
        self.pixmap = QPixmap('.\\data\\ghibli.jpg')

        self.painted_info_lbl = QLabel(self)
        self.painted_value_lbl = QLabel(self)
        self.left_info_lbl = QLabel(self)
        self.left_value_lbl = QLabel(self)
        self.all_info_lbl = QLabel(self)
        self.all_value_lbl = QLabel(self)

        self.grid = QGridLayout(self)

        self.vbox = QVBoxLayout(self)

        self._settings()

    def _settings(self):

        self.picture.setPixmap(self.pixmap.scaledToHeight(600))

        self.painted_info_lbl.setText("Painter pixels:")
        self.painted_value_lbl.setText("0 (hard)")
        self.left_info_lbl.setText("Left pixels:")
        self.left_value_lbl.setText("10 (hard)")
        self.all_info_lbl.setText("All pixels:")
        self.all_value_lbl.setText("322 (hard)")

        self.grid.addWidget(self.painted_info_lbl, 0, 0)
        self.grid.addWidget(self.painted_value_lbl, 0, 1)
        self.grid.addWidget(self.left_info_lbl, 1, 0)
        self.grid.addWidget(self.left_value_lbl, 1, 1)
        self.grid.addWidget(self.all_info_lbl, 2, 0)
        self.grid.addWidget(self.all_value_lbl, 2, 1)

        self.vbox.addWidget(self.picture)
        self.vbox.addLayout(self.grid)

        self.setLayout(self.vbox)