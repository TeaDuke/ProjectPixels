import json

from data_classes.Base import Base
from pathlib import Path

from data_classes.Save import Save
from data_services.save_data_service import SaveDataService
from data_services.task_data_service import TaskDataService


class BaseDataService:

    @staticmethod
    def get_current_save():
        with open(f"data\\base.json", 'r', encoding='utf-8') as f:
            base_json = json.load(f)
        base = Base.from_dict(base_json)
        return base.current_save

    @staticmethod
    def update_current_save(save_title: str):
        with open(f"data\\base.json", 'r', encoding='utf-8') as f:
            base_json = json.load(f)
        base = Base.from_dict(base_json)
        base.current_save = save_title
        base_json = base.to_dict()
        with open(f"data\\base.json", 'w', encoding='utf-8') as f:
            json.dump(base_json, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_saves():
        with open(f"data\\base.json", 'r', encoding='utf-8') as f:
            base_json = json.load(f)
        base = Base.from_dict(base_json)
        return base.saves

    @staticmethod
    def update_saves(saves):
        with open(f"data\\base.json", 'r', encoding='utf-8') as f:
            base_json = json.load(f)
        base = Base.from_dict(base_json)
        base.saves = saves
        base_json_new = base.to_dict()
        with open(f"data\\base.json", 'w', encoding='utf-8') as f:
            json.dump(base_json_new, f, ensure_ascii=False, indent=2)

    @staticmethod
    def create_new_save(title: str):
        saves = BaseDataService.get_saves()
        saves.append(title)

        folder_path = Path(f"data\\{title}")
        folder_path.mkdir(parents=True, exist_ok=True)
        picture_folder_path = Path(f"data\\{title}\\pictures")
        picture_folder_path.mkdir(parents=True, exist_ok=True)

        BaseDataService._create_save_data(title, folder_path)
        BaseDataService._create_tasks_data(title, folder_path)

        BaseDataService.update_saves(saves)
        BaseDataService.update_current_save(title)

    @staticmethod
    def _create_save_data(title, folder_path):
        save = Save(title)
        data_path = folder_path / f"save.json"
        data_path.write_text("")
        SaveDataService.update_save(title, save)

    @staticmethod
    def _create_tasks_data(title, folder_path):
        data_path = folder_path / f"tasks.json"
        data_path.write_text("")
        TaskDataService.create_tasks_file(title)