import random
from numbers import Number

import numpy
from PyQt6.QtGui import QImage

from data_classes.Picture import Picture
from data_services.base_data_service import BaseDataService
from data_services.picture_data_service import PictureDataService
from data_services.save_data_service import SaveDataService
from enums.status_enum import StatusEnum


class PictureMainService:

    @staticmethod
    def add_new_picture(pic_path):
        current_save = BaseDataService.get_current_save()
        new_id = PictureDataService.add_new_picture(current_save, pic_path)
        current_pic_id = SaveDataService.get_current_picture_id(current_save)
        current_pic_info =  PictureDataService.get_picture_info(current_save, current_pic_id)
        if new_id != current_pic_id and current_pic_info.status == StatusEnum.FINISHED:
            PictureMainService.update_current_picture_id(new_id)


    @staticmethod
    def delete_picture(pid: int):
        current_save = BaseDataService.get_current_save()
        PictureDataService.delete_picture(current_save, pid)

    @staticmethod
    def open_pixels(number: Number):
        if number == 0:
            return
        # get picture id, progress picture, picture info and opening mode
        current_save = BaseDataService.get_current_save()
        pic_id = SaveDataService.get_current_picture_id(current_save)
        ppic = PictureDataService.get_progress_picture(current_save, pic_id)
        pic_info = PictureDataService.get_picture_info(current_save, pic_id)

        opening_mode = SaveDataService.get_opening_mode(current_save)

        # open pixels
        if opening_mode == 'line':
            PictureMainService._open_pixels_logic_line(number, ppic, pic_info)
        elif opening_mode == 'random':
            PictureMainService._open_pixels_logic_random(number, ppic, pic_info)
        # set FINISHED status, if picture is opened
        if pic_info.opened_pixels == pic_info.all_pixels:
            pic_info.status = StatusEnum.FINISHED
            new_current_pic_id = PictureMainService.find_new_current_picture()
            if new_current_pic_id != 0:
                PictureMainService.update_current_picture_id(new_current_pic_id)

        # update picture info and progress picture
        PictureDataService.update_picture_info(current_save, pic_info)
        PictureDataService.update_progress_picture(current_save, pic_id, ppic)

    @staticmethod
    def _open_pixels_logic_line(number, ppic, pic_info: Picture):
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

    @staticmethod
    def update_current_picture_id(current_picture_id):
        current_save = BaseDataService.get_current_save()

        # update status of old current picture
        old_current_picture_id = SaveDataService.get_current_picture_id(current_save)
        old_current_picture_info = PictureDataService.get_picture_info(current_save, old_current_picture_id)
        if old_current_picture_info.status == StatusEnum.IN_PROGRESS:
            old_current_picture_info.status = StatusEnum.STOPPED
        PictureDataService.update_picture_info(current_save, old_current_picture_info)

        # update current picture
        SaveDataService.update_current_picture_id(current_save, current_picture_id)

        # update status of new current picture
        new_current_picture_info = PictureDataService.get_picture_info(current_save, current_picture_id)
        if new_current_picture_info.status == StatusEnum.STOPPED:
            new_current_picture_info.status = StatusEnum.IN_PROGRESS
        PictureDataService.update_picture_info(current_save, new_current_picture_info)

    @staticmethod
    def find_new_current_picture():
        current_save = BaseDataService.get_current_save()

        new_p_id = 0
        pictures_ids = SaveDataService.get_pictures_ids(current_save)
        current_id = SaveDataService.get_current_picture_id(current_save)
        for pid in pictures_ids:
            pic_info = PictureMainService.get_picture_info(pid)
            if pid != current_id and pic_info.status == StatusEnum.STOPPED:
                new_p_id = pid
                break
        if new_p_id == 0:
            for pid in pictures_ids:
                if pid != current_id:
                    new_p_id = pid
                    break
        return new_p_id





