class Task:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def from_dict(data):
        return Task(data["name"], data["price"])