from data_services.task_data_service import TaskDataService

class TaskMainService():

    @staticmethod
    def getTasks():
        return TaskDataService.getTasks("Hollow")

    @staticmethod
    def addTask(task):
        return TaskDataService.addTask("Hollow", task)