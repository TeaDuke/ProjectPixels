import json

from data_classes.Base import Base


class BaseDataService:

    @staticmethod
    def get_current_save():
        with open(f"data\\base.json", 'r', encoding='utf-8') as f:
            base_json = json.load(f)
        base = Base.from_dict(base_json)
        return base.current_save

    @staticmethod
    def get_saves():
        with open(f"data\\base.json", 'r', encoding='utf-8') as f:
            base_json = json.load(f)
        base = Base.from_dict(base_json)
        return base.saves