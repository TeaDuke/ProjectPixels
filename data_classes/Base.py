class Base:

    def __init__(self):
        self.saves = []
        self.current_save = ""

    def to_dict(self):
        return {
            "saves": self.saves,
            "current_save": self.current_save
        }

    @staticmethod
    def from_dict(data):
        base = Base()
        base.saves = data.get('saves', [])
        base.current_save = data.get('current_save', '')
        return base
