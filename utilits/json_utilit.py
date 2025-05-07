import json

from data_classes.Task import Task

filename = input("write filename for pickle file:\n")
data = [
    Task("зарядка", 2),
    Task("читать", 3),
    Task("почистить зубы", 1),
    Task("не есть сладкое", 7),
    Task("учиться (уник)", 5),
    Task("помолиться", 1)
]

json_data = {"tasks": [task.to_dict() for task in data]}

with open(f"{filename}.json", 'w', encoding="utf-8") as f:
  json.dump(json_data, f, ensure_ascii=False, indent=2)
