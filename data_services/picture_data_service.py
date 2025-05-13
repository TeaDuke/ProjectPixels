import json

import numpy
from PIL import Image
from PyQt6.QtGui import QImage

from data_classes.Picture import Picture


class PictureDataService:

    @staticmethod
    def get_picture_info(save_title, p_id):
        with open(f"data\\{save_title}\\pictures\\{p_id}\\d-{p_id}.json", 'r', encoding='utf-8') as f:
            picture_json = json.load(f)
        picture = Picture.from_dict(picture_json)
        return picture

    @staticmethod
    def update_picture_info(save_title, p_id, picture):
        picture_json = picture.to_dict()
        with open(f"data\\{save_title}\\pictures\\{p_id}\\d-{p_id}.json", 'w', encoding='utf-8') as f:
            json.dump(picture_json, f, ensure_ascii=False, indent=2)

    @staticmethod
    def get_progress_picture(save_title, p_id):
        pic = QImage(f"data\\{save_title}\\pictures\\{p_id}\\p-{p_id}.png")
        return pic.convertToFormat(QImage.Format.Format_RGBA8888)

    @staticmethod
    def update_progress_picture(save_title, p_id, ppic):
        ppic.save(f"data\\{save_title}\\pictures\\{p_id}\\p-{p_id}.png")
