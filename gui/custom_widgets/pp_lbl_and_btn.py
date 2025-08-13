from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout

from consts import TEXT, TEXT_SIZE
from gui.custom_widgets.pp_button import PPButton


class PPLblAndBtn(QWidget):

    btn_clicked = pyqtSignal()

    def __init__(self, btn_type: str):
        super().__init__()

        self.lbl = QLabel()
        self.pp_btn = PPButton(self, btn_type)
        self.grid = QGridLayout()

        self._settings()
        self.setCss()

    def _settings(self):
        self.lbl.setText("Something")
        self.lbl.setMinimumWidth(200)

        self.pp_btn.clicked.connect(lambda : self.btn_clicked.emit())

        self.grid.addWidget(self.lbl, 0, 0)
        self.grid.addWidget(self.pp_btn, 0, 1)

        self.setLayout(self.grid)

    def setCss(self):
        self.setStyleSheet(f"""
            QLabel
            {{
                color: {TEXT};
                font-size: {TEXT_SIZE}
            }}
        """)

    def setTextToLbl(self, text: str):
        self.lbl.setText(text)

    def setTextToBtn(self, text:str):
        self.pp_btn.setText(text)