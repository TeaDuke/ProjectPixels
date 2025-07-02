class Task:

    def __init__(self, tid, name, price):
        self.tid = tid
        self.name = str(name)
        self.price = int(price)

    def update_name(self, name):
        self.name = str(name)

    def update_price(self, price):
        self.price = int(price)

    def to_dict(self):
        return {"tid": self.tid, "name": self.name, "price": self.price}

    @staticmethod
    def from_dict(data):
        return Task(data["tid"], data["name"], data["price"])

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.tid == other.tid
        return False

    def __repr__(self):
        return f"Task({self.name})"
