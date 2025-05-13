from data_services.base_data_service import BaseDataService
from data_services.task_data_service import TaskDataService

class TaskMainService:

    @staticmethod
    def getTasks():
        current_save = BaseDataService.get_current_save()
        return TaskDataService.getTasks(current_save)

    @staticmethod
    def addTask(task):
        current_save = BaseDataService.get_current_save()
        return TaskDataService.addTask(current_save, task)