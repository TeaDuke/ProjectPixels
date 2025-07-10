from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QSizePolicy, QTabBar, QPushButton, QComboBox

from gui.pixels_info import PixelsInfo
from gui.settings import Settings
from gui.task_list import TaskList
from services.base_main_service import BaseMainService


class MainWindow(QWidget):

    current_save_changed = pyqtSignal(str)
    open_create_save = pyqtSignal()

    saves = []
    current_save = ""

    def __init__(self):
        super().__init__()

        # declare widgets
        self.tabbar = QTabBar()

        self.settings_window = Settings()

        self.saves_combo = QComboBox()
        self.new_save_btn = QPushButton()

        self.pxinfo = PixelsInfo()
        self.tasklist = TaskList()

        self.vbox = QVBoxLayout()

        self._settings()

    def _settings(self):
        self.resize(600,600)

        self.saves = BaseMainService.get_saves()
        self.current_save = BaseMainService.get_current_save()

        self.tabbar.addTab("Settings")
        self.tabbar.tabBarClicked.connect(self.tab_clicked)

        self.saves_combo.addItems(self.saves)
        self.saves_combo.setCurrentText(self.current_save)
        self.saves_combo.currentTextChanged.connect(lambda: self._change_current_save(self.saves_combo.currentText()))

        self.new_save_btn.setText("Create new Save")
        self.new_save_btn.clicked.connect(self._open_create_save)

        self.tasklist.tasks_saved.connect(self.update_pixels_info)

        self.vbox.addWidget(self.tabbar)
        self.vbox.addWidget(self.saves_combo)
        self.vbox.addWidget(self.new_save_btn)
        self.vbox.addWidget(self.pxinfo)
        self.vbox.addWidget(self.tasklist)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.vbox)

    def update_pixels_info(self):
        self.pxinfo.update_pixels_info()

    def tab_clicked(self, index):
        self.settings_window.update_settings()
        self.settings_window.show()

    def _change_current_save(self, title):
        self.current_save_changed.emit(title)
        self.settings_window.close()
        self.tasklist.close_windows()
        self.pxinfo.close_windows()
        self.close()

    def _open_create_save(self):
        self.open_create_save.emit()
        self.settings_window.close()
        self.tasklist.close_windows()
        self.pxinfo.close_windows()
        self.close()