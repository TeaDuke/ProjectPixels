from data_services.base_data_service import BaseDataService


class BaseMainService:

    @staticmethod
    def create_data_folder():
        BaseDataService.create_data_folder()

    @staticmethod
    def create_base_json():
        BaseDataService.create_base_json()

    @staticmethod
    def create_new_save(title: str):
        BaseDataService.create_new_save(title)

    @staticmethod
    def get_current_save():
        return BaseDataService.get_current_save()

    @staticmethod
    def update_current_save(save_title):
        BaseDataService.update_current_save(save_title)

    @staticmethod
    def get_saves():
        return BaseDataService.get_saves()