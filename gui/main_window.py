from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, \
    QHBoxLayout, QFrame

from consts import BACKGROUND, BACKGROUND_LIGHTER
from gui.custom_widgets.pp_button import PPButton
from gui.custom_widgets.pp_dropdown import PPDropDown
from gui.custom_widgets.pp_icon_button import PPIconButton
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

        self.pp_saves_combo = PPDropDown()
        self.pp_create_save_btn = PPButton(self, "stroke")
        self.pp_settings_btn = PPIconButton("stroke", "settings")

        self.settings_window = Settings()

        self.pxinfo = PixelsInfo()
        self.tasklist = TaskList(self)

        self.line1 = QFrame()
        self.line2 = QFrame()

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self._settings()
        self.set_css()

    def _settings(self):
        self.setWindowTitle("Project Pixels")
        self.resize(600,600)


        self.saves = BaseMainService.get_saves()
        self.current_save = BaseMainService.get_current_save()

        self.pp_saves_combo.set_items(self.saves)
        self.pp_saves_combo.set_current_text(self.current_save)
        self.pp_saves_combo.currentTextChanged.connect(lambda: self._change_current_save(self.pp_saves_combo.get_current_text()))

        self.pp_create_save_btn.setText("Create new save")
        self.pp_create_save_btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.pp_create_save_btn.clicked.connect(self._open_create_save)

        self.pp_settings_btn.clicked.connect(self.open_settings)

        self.tasklist.tasks_saved.connect(self.update_pixels_info)
        self.tasklist.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.line1.setFrameShape(QFrame.Shape.HLine)
        self.line1.setStyleSheet(f"""QFrame{{color: {BACKGROUND_LIGHTER};}}""")
        self.line2.setFrameShape(QFrame.Shape.HLine)
        self.line2.setStyleSheet(f"""QFrame{{color: {BACKGROUND_LIGHTER};}}""")

        self.hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.hbox.setSpacing(20)
        self.hbox.setContentsMargins(0,0,0,0)
        self.hbox.addWidget(self.pp_saves_combo)
        self.hbox.addWidget(self.pp_create_save_btn)
        self.hbox.addStretch()
        self.hbox.addWidget(self.pp_settings_btn)

        self.vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vbox.setContentsMargins(20,20,20,20)
        self.vbox.setSpacing(20)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.pxinfo)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.tasklist)

        self.setLayout(self.vbox)

    def set_css(self):
        self.setStyleSheet(f"""
            MainWindow
            {{
                background-color: {BACKGROUND};
            }}
        """)

    def update_pixels_info(self):
        self.pxinfo.update_pixels_info()

    def open_settings(self, index):
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