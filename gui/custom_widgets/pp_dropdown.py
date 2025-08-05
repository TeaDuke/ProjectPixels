from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QComboBox, QWidget, QMenu, QHBoxLayout
from colors import *
from gui.custom_widgets.pp_button import PPButton
from utilits.image_utilits import resource_path


class PPDropDown (QWidget):

    selected_text = ""
    items = []
    actions = []

    def __init__(self):
        super().__init__()

        self.pp_btn = PPButton("stroke")
        self.menu = QMenu(self)

        self.hbox = QHBoxLayout()

        self._settings()
        self.setCss()

    def _settings(self):

        self.pp_btn.setIcon(QIcon(resource_path("chevron-down.svg")))
        self.pp_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pp_btn.clicked.connect(self.show_menu)

        self.hbox.addWidget(self.pp_btn)

        self.setLayout(self.hbox)

    def setCss(self):
        self.setStyleSheet(f"""
            QMenu
            {{
                background-color: {BACKGROUND_DARKER};
                border-radius: 8px;
                padding: 10px;
                font-size: 18px;
                color: {TEXT};
            }}
            QMenu::item
            {{
                border: 5px solid {BACKGROUND_DARKER};
                border-radius: 8px;
                margin: 5px 0;
            }}
            QMenu:last-child
            {{
                margin: 5px 0;
            }}
            QMenu::item:selected
            {{
                background-color: {PRIMARY};
                border: 5px solid {PRIMARY};
            }}
        """)

    def setItems(self, items):
        self.items = items
        for item in items:
            action = QAction(item, self)
            action.setIcon(QIcon(resource_path("check.svg")))
            action.setIconVisibleInMenu(False)
            action.triggered.connect(lambda checked, text=item: self.select_item(text))
            self.actions.append(action)
            self.menu.addAction(action)

    def setCurrentText(self, text):
        if text in self.items:
            self.select_item(text)

    def show_menu(self):
        btn_rect = self.pp_btn.rect()
        glPos = self.pp_btn.mapToGlobal(btn_rect.topLeft())
        newPos = glPos - QPoint(10, 15)
        self.menu.move(newPos)
        self.menu.setMinimumWidth(self.pp_btn.width()+20)
        self.menu.exec()

    def select_item(self, text):
        if self.selected_text != "":
            action = self.actions[self._findIndexByText(self.selected_text)]
            action.setIconVisibleInMenu(False)
        self.selected_text = text
        action_ = self.actions[self._findIndexByText(text)]
        action_.setIconVisibleInMenu(True)
        self.pp_btn.setText(self.selected_text)

    def getCurrentText(self):
        return self.selected_text

    def _findIndexByText(self, text):
        index = self.items.index(text)
        return index