import json
import shutil

import numpy
from PIL import Image
from PyQt6.QtGui import QImage
from pathlib import Path

from data_classes.Picture import Picture
from data_services.save_data_service import SaveDataService
from utilits.array_utilits import get_max_number_from_array


class PictureDataService:

    @staticmethod
    def add_new_picture(save_title, path):
        ids = SaveDataService.get_picture_ids(save_title)
        if len(ids) != 0:
            new_id = get_max_number_from_array(ids) + 1
        else:
            new_id = 1
        ids.append(new_id)

        source = Path(path)
        folder_path = Path(f"data\\{save_title}\\pictures\\{new_id}")
        folder_path.mkdir(parents=True, exist_ok=True)
        image_dst = folder_path / f"i-{new_id}.png"
        shutil.copy(source, image_dst)

        PictureDataService._create_progress_picture(save_title, new_id)
        PictureDataService._create_picture_data(save_title, new_id, source.name, folder_path)

        SaveDataService.update_picture_ids(save_title, ids)
        if new_id == 1:
            SaveDataService.update_current_picture_id(save_title, new_id)

    @staticmethod
    def _create_progress_picture(save_title, new_id):
        ppic = Image.open(f"data\\{save_title}\\pictures\\{new_id}\\i-{new_id}.png").convert("RGBA")

        data = numpy.array(ppic)
        data[:,:,3] = 0

        ppic = Image.fromarray(data)
        ppic.save(f"data\\{save_title}\\pictures\\{new_id}\\p-{new_id}.png")

    @staticmethod
    def _create_picture_data(save_title, new_id, filename, folder_path):
        ppic = PictureDataService.get_progress_picture(save_title, new_id)

        pic_info = Picture()
        pic_info.filename = filename
        pic_info.id = new_id
        pic_info.height = ppic.height()
        pic_info.width = ppic.width()

        data_path = folder_path / f"d-{new_id}.json"
        data_path.write_text("")
        PictureDataService.update_picture_info(save_title, new_id, pic_info)

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
