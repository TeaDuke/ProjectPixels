import json

from data_classes.Save import Save
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