from data_classes.Save import Save
import json


class SaveDataService:

    @staticmethod
    def update_save(save_title, save: Save):
        save_json = save.to_dict()
        with open(f"data\\{save_title}\\save.json", 'w', encoding='utf-8') as f:
            json.dump(save_json, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_current_picture_id(save_title):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        return save.current_picture_id

    @staticmethod
    def update_current_picture_id(save_title, current_picture_id):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        save.current_picture_id = current_picture_id
        save_json_new = save.to_dict()
        with open(f"data\\{save_title}\\save.json", 'w', encoding='utf-8') as f:
            json.dump(save_json_new, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_picture_ids(save_title):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        return save.pictures_ids

    @staticmethod
    def update_picture_ids(save_title, pictures_ids):
        with open(f"data\\{save_title}\\save.json", 'r', encoding='utf-8') as f:
            save_json = json.load(f)
        save = Save.from_dict(save_json)
        save.pictures_ids = pictures_ids
        save_json_new = save.to_dict()
        with open(f"data\\{save_title}\\save.json", 'w', encoding='utf-8') as f:
            json.dump(save_json_new, f, ensure_ascii=False, indent=2)

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



