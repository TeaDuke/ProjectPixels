from data_services.base_data_service import BaseDataService
from data_services.task_data_service import TaskDataService

class TaskMainService:

    @staticmethod
    def get_tasks():
        current_save = BaseDataService.get_current_save()
        return TaskDataService.get_tasks(current_save)

    @staticmethod
    def add_task(task):
        current_save = BaseDataService.get_current_save()
        TaskDataService.add_task(current_save, task)

    @staticmethod
    def delete_task(task):
        current_save = BaseDataService.get_current_save()
        TaskDataService.delete_task(current_save, task)

    @staticmethod
    def update_task(task):
        current_save = BaseDataService.get_current_save()
        TaskDataService.update_task(current_save, task)

    @staticmethod
    def get_new_tid():
        current_save = BaseDataService.get_current_save()
        tasks = sorted(TaskDataService.get_tasks(current_save), key=lambda task: task.tid, reverse=True)
        return tasks[0].tid + 1