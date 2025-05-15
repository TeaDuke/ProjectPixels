from numbers import Number

from data_classes.Picture import Picture
from data_services.base_data_service import BaseDataService
from data_services.picture_data_service import PictureDataService
from data_services.save_data_service import SaveDataService


class PictureMainService:

    @staticmethod
    def open_pixels(number: Number):
        current_save = BaseDataService.get_current_save()
        pic_id = SaveDataService.get_current_picture_id(current_save)
        ppic = PictureDataService.get_progress_picture(current_save, pic_id)
        pic_info = PictureDataService.get_picture_info(current_save, pic_id)

        PictureMainService._open_pixels_logic(number, ppic, pic_info)

        PictureDataService.update_picture_info(current_save, pic_id, pic_info)
        PictureDataService.update_progress_picture(current_save, pic_id, ppic)

    @staticmethod
    def _open_pixels_logic(number, ppic, pic_info: Picture): #TODO: check work of this function
        row = pic_info.opened_pixels // pic_info.width
        col = pic_info.opened_pixels % pic_info.width
        for r in range(row, pic_info.height):
            for c in range(col, pic_info.width):
                with open('services\\log1.txt', 'a', encoding='utf-8') as f:
                    f.write(f"r - {r}, c - {c}, number - {number}")
                color = ppic.pixelColor(c, r)
                color.setAlpha(255)
                ppic.setPixelColor(c, r, color)
                number -= 1
                pic_info.opened_pixels += 1
                if number == 0:
                    break
            col = 0
            if number == 0:
                break

    @staticmethod
    def get_picture_info():
        current_save = BaseDataService.get_current_save()
        pic_id = SaveDataService.get_current_picture_id(current_save)
        return PictureDataService.get_picture_info(current_save, pic_id)

    @staticmethod
    def get_progress_picture():
        current_save = BaseDataService.get_current_save()
        pic_id = SaveDataService.get_current_picture_id(current_save)
        return PictureDataService.get_progress_picture(current_save, pic_id)