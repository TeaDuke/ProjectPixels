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
        TaskDataService.addTask(current_save, task)

    @staticmethod
    def deleteTask(task):
        current_save = BaseDataService.get_current_save()
        TaskDataService.deleteTask(current_save, task)

    @staticmethod
    def updateTask(task):
        current_save = BaseDataService.get_current_save()
        TaskDataService.updateTask(current_save, task)

    @staticmethod
    def getNewTid():
        current_save = BaseDataService.get_current_save()
        tasks = sorted(TaskDataService.getTasks(current_save), key=lambda task: task.tid, reverse=True)
        return tasks[0].tid + 1