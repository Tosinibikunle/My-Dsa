class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.mul = 1
        self.add = 0
        self.arr = []

    def append(self, val):
        inv = pow(self.mul, self.MOD - 2, self.MOD)
        stored = (val - self.add) % self.MOD
        stored = (stored * inv) % self.MOD
        self.arr.append(stored)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m) ->:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD
