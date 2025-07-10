from gui.create_save import CreateSave
from gui.main_window import MainWindow
from services.base_main_service import BaseMainService


class StartUp:

    def __init__(self):
        self.main_window = None
        self.create_save = None

        self._settings()

    def _settings(self):

        BaseMainService.create_data_folder()
        BaseMainService.create_base_json()

        self._start()

    def _start(self):
        if BaseMainService.get_current_save() == "":
            self._open_create_save()
        else:
            self._open_main_window()

    def _open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.current_save_changed.connect(self._change_current_save)
        self.main_window.open_create_save.connect(self._open_create_save)
        self.main_window.show()

    def _change_current_save(self, title):
        del self.main_window
        self.main_window = None
        del self.create_save
        self.create_save = None

        BaseMainService.update_current_save(title)
        self._open_main_window()

    def _open_create_save(self):
        del self.main_window
        self.main_window = None

        self.create_save = CreateSave()
        self.create_save.current_save_chosen.connect(self._change_current_save)
        self.create_save.show()