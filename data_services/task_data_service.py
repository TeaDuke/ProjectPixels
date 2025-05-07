import json
import pickle

from data_classes.Task import Task


class TaskDataService:

    @staticmethod
    def getTasks(save_title):
        with open(f"data\\{save_title}\\tasks.json", 'r', encoding='utf-8') as f:
            loaded_tasks = json.load(f)
        tasks = [Task.from_dict(t) for t in loaded_tasks['tasks']]
        return tasks

    @staticmethod
    def addTask(save_title, task):
        tasks = TaskDataService.getTasks(save_title)
        tasks.append(task)
        json_tasks = {"tasks": [task.to_dict() for task in tasks]}
        with open(f"data\\{save_title}\\tasks.json", 'w', encoding='utf-8') as f:
            json.dump(json_tasks, f, ensure_ascii=False, indent=2)

