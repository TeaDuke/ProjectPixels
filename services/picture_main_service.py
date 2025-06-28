import random
from numbers import Number

import numpy
from PyQt6.QtGui import QImage

from data_classes.Picture import Picture
from data_services.base_data_service import BaseDataService
from data_services.picture_data_service import PictureDataService
from data_services.save_data_service import SaveDataService


class PictureMainService:

    @staticmethod
    def add_new_picture(pic_path):
        current_save = BaseDataService.get_current_save()
        PictureDataService.add_new_picture(current_save, pic_path)

    @staticmethod
    def open_pixels(number: Number):
        if number == 0:
            return

        current_save = BaseDataService.get_current_save()
        pic_id = SaveDataService.get_current_picture_id(current_save)
        ppic = PictureDataService.get_progress_picture(current_save, pic_id)
        pic_info = PictureDataService.get_picture_info(current_save, pic_id)

        opening_mode = SaveDataService.get_opening_mode(current_save)

        if opening_mode == 'line':
            PictureMainService._open_pixels_logic_line(number, ppic, pic_info)
        elif opening_mode == 'random':
            PictureMainService._open_pixels_logic_random(number, ppic, pic_info)

        PictureDataService.update_picture_info(current_save, pic_id, pic_info)
        PictureDataService.update_progress_picture(current_save, pic_id, ppic)

    @staticmethod
    def _open_pixels_logic_line(number, ppic, pic_info: Picture): #TODO: check work of this function
        row = pic_info.line_position // pic_info.width
        col = pic_info.line_position % pic_info.width
        for r in range(row, pic_info.height):
            for c in range(col, pic_info.width):
                pic_info.line_position += 1
                color = ppic.pixelColor(c, r)
                if color.alpha() == 255:
                    continue
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
    def _open_pixels_logic_random(number, ppic, pic_info: Picture):
        buf = ppic.bits()
        buf.setsize(ppic.sizeInBytes())
        data = numpy.frombuffer(buf, dtype=numpy.uint8).reshape((pic_info.height, pic_info.width, 4))
        closed_pixels = list(zip(*numpy.where(data[:,:,3] == 0)))
        random.shuffle(closed_pixels)
        while number > 0 and closed_pixels:
            y, x = closed_pixels.pop()
            data[y,x,3] = 255
            number -= 1
            pic_info.opened_pixels += 1
        ppic = QImage(data.data, pic_info.width, pic_info.height, QImage.Format.Format_RGBA8888)

    @staticmethod
    def get_picture_info(pic_id = 0):
        current_save = BaseDataService.get_current_save()
        if pic_id == 0:
            pic_id = SaveDataService.get_current_picture_id(current_save)
        return PictureDataService.get_picture_info(current_save, pic_id)

    @staticmethod
    def get_progress_picture(pic_id = 0):
        current_save = BaseDataService.get_current_save()
        if pic_id == 0:
            pic_id = SaveDataService.get_current_picture_id(current_save)
        return PictureDataService.get_progress_picture(current_save, pic_id)


