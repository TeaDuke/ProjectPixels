from data_services.base_data_service import BaseDataService
from data_services.save_data_service import SaveDataService


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
        return SaveDataService.get_picture_ids(current_save)