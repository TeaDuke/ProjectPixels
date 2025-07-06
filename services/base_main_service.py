from data_services.base_data_service import BaseDataService


class BaseMainService:

    @staticmethod
    def create_new_save(title: str):
        BaseDataService.create_new_save(title)

    @staticmethod
    def get_current_save():
        return BaseDataService.get_current_save()

    @staticmethod
    def get_saves():
        return BaseDataService.get_saves()