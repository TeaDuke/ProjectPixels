import json

from data_classes.Picture import Picture


class PictureDataService:

    @staticmethod
    def get_picture_info(save_title, id):
        with open(f"data\\{save_title}\\pictures\\{id}\\d-{id}.json", 'r', encoding='utf-8') as f:
            picture_json = json.load(f)
        picture = Picture.from_dict(picture_json)
        return picture

    @staticmethod
    def edit_picture_info(save_title, id, picture):
        picture_json = picture.to_dict()
        with open(f"data\\{save_title}\\pictures\\{id}\\d-{id}.json", 'w', encoding='utf-8') as f:
            json.dump(picture_json, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_progress_picture(save_title, id):
        with open(f"data\\{save_title}\\pictures\\{id}\\d-{id}.json", 'r', encoding='utf-8') as f:
            picture_json = json.load(f)
        picture = Picture.from_dict(picture_json)
        return picture