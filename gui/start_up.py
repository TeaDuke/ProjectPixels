from gui.create_save import CreateSave
from gui.main_window import MainWindow
from services.base_main_service import BaseMainService


class StartUp:

    def __init__(self):
        self.main_window = MainWindow()
        self.create_save = CreateSave()

        self._settings()

    def _settings(self):

        self.main_window.resize(400, 400)
        self.create_save.resize(400, 400)

        self._start()


    def _start(self):
        if BaseMainService.get_current_save() == "":
            self.create_save.show()
        else:
            self.create_save.show()
            # self.main_window.show()