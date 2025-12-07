class MyHashSet:
    def __init__(self):
        self.d = {}

    def add(self, key: int):
        self.d[key] = 1

    def remove(self, key: int):
        self.d[key] = 0

    def contains(self, key: int):
        return self.d.get(key, 0) != 0
