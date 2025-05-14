class Task:

    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

    def to_dict(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def from_dict(data):
        return Task(data["name"], data["price"])

    def __eq__(self, other): #TODO: change this system later to id
        if isinstance(other, Task):
            return self.name == other.name
        return False

    def __repr__(self):
        return f"Task({self.name})"
