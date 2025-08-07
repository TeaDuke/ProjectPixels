from data_services.base_data_service import BaseDataService
from data_services.picture_data_service import PictureDataService
from data_services.save_data_service import SaveDataService
from enums.status_enum import StatusEnum
from services.picture_main_service import PictureMainService


class SaveMainService:

    @staticmethod
    def get_opening_mode():
        current_save = BaseDataService.get_current_save()
        return SaveDataService.get_opening_mode(current_save)

    @staticmethod
    def update_opening_mode(op_mode):
        current_save = BaseDataService.get_current_save()
        SaveDataService.update_opening_mode(current_save, op_mode)

    @staticmethod
    def get_pictures_ids():
        current_save = BaseDataService.get_current_save()
        return SaveDataService.get_pictures_ids(current_save)

    @staticmethod
    def get_current_picture_id():
        current_save = BaseDataService.get_current_save()
        return SaveDataService.get_current_picture_id(current_save)



