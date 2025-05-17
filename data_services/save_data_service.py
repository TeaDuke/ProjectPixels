from data_classes.Save import Save
import json
from data_services.base_data_service import BaseDataService


class SaveDataService:

    @staticmethod
    def get_current_picture_id(save_title):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        return save.current_picture_id
    @staticmethod
    def get_picture_ids(save_title):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        return save.pictures_ids

    @staticmethod
    def get_opening_mode(save_title):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        return save.opening_mode

    @staticmethod
    def update_opening_mode(save_title, op_mode):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        save.opening_mode = op_mode
        save_json_new = save.to_dict()
        with open(f"data\\{save_title}\\save.json", 'w', encoding='utf-8') as f:
            json.dump(save_json_new, f, ensure_ascii=False, indent=2)



