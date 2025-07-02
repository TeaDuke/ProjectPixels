import json
import pickle

from data_classes.Task import Task

class TaskDataService:

    @staticmethod
    def getTasks(save_title):
        with open(f"data\\{save_title}\\tasks.json", 'r', encoding='utf-8') as f:
            tasks_json = json.load(f)
        tasks = [Task.from_dict(t) for t in tasks_json['tasks']]
        return tasks

    @staticmethod
    def addTask(save_title, task):
        tasks = TaskDataService.getTasks(save_title)
        tasks.append(task)
        json_tasks = {"tasks": [task.to_dict() for task in tasks]}
        with open(f"data\\{save_title}\\tasks.json", 'w', encoding='utf-8') as f:
            json.dump(json_tasks, f, ensure_ascii=False, indent=2)

    @staticmethod
    def deleteTask(save_title, task):
        tasks = TaskDataService.getTasks(save_title)
        tasks.remove(task)
        json_tasks = {"tasks": [task.to_dict() for task in tasks]}
        with open(f"data\\{save_title}\\tasks.json", 'w', encoding='utf-8') as f:
            json.dump(json_tasks, f, ensure_ascii=False, indent=2)

    @staticmethod
    def updateTask(save_title, task):
        tasks = TaskDataService.getTasks(save_title)
        ind = tasks.index(task)
        tasks[ind] = task
        json_tasks = {"tasks": [task.to_dict() for task in tasks]}
        with open(f"data\\{save_title}\\tasks.json", 'w', encoding='utf-8') as f:
            json.dump(json_tasks, f, ensure_ascii=False, indent=2)
