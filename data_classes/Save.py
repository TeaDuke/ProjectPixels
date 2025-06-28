class Save:

    def __init__(self, title="antihype"):
        self.title = title
        self.pictures_ids = []
        self.current_picture_id = 0
        self.opening_mode = "" # line or random

    def to_dict(self):
        return {
            "title": self.title,
            "pictures_ids": self.pictures_ids,
            "current_picture_id": self.current_picture_id,
            "opening_mode": self.opening_mode
        }

    @staticmethod
    def from_dict(data):
        save = Save()
        save.title = data.get('title', '')
        save.pictures_ids = data.get('pictures_ids', [])
        save.current_picture_id = data.get('current_picture_id', 0)
        save.opening_mode = data.get('opening_mode', '')
        return save
