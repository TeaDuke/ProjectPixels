from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QHBoxLayout, QPushButton


class TaskCreator(QWidget):

    def __init__(self):
        super().__init__()

        self.title_lbl = QLabel()

        self.name_info_lbl = QLabel()
        self.name_value_le = QLineEdit()
        self.price_info_lbl = QLabel()
        self.price_value_le = QLineEdit()

        self.create_btn = QPushButton()
        self.cancel_btn = QPushButton()

        self.grid = QGridLayout()

        self.hbox = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.title_lbl.setText("Create task")

        self.name_info_lbl.setText("Name:")
        self.price_info_lbl.setText("Price (in pixels):")

        self.create_btn.setText("Create")
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.clicked.connect(self.close)

        self.grid.addWidget(self.name_info_lbl, 0, 0)
        self.grid.addWidget(self.name_value_le, 0, 1)
        self.grid.addWidget(self.price_info_lbl, 1, 0)
        self.grid.addWidget(self.price_value_le, 1, 1)

        self.hbox.addWidget(self.create_btn)
        self.hbox.addWidget(self.cancel_btn)

        self.vbox.addWidget(self.title_lbl)
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

