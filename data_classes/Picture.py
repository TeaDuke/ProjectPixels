class Picture:

    def __init__(self):
        self.filename = ""
        self.id = 0
        self.height = 0
        self.width = 0
        self.opened_pixels = 0

    @property
    def all_pixels(self):
        return self.height * self.width

    def to_dict(self):
        return {
            "filename": self.filename,
            "id": self.id,
            "height": self.height,
            "width": self.width,
            "opened_pixels": self.opened_pixels
        }

    @staticmethod
    def from_dict(data):
        picture = Picture()
        picture.filename = data.get('filename', '')
        picture.id = data.get('id', 0)
        picture.height = data.get('height', '')
        picture.width = data.get('width', '')
        picture.opened_pixels = data.get('opened_pixels', 0)
        return picture