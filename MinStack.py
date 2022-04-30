class MinStack:
    def __init__(self):
        self.store = []
        self.min_index = None

    def push(self, val: int) -> None:
        self.store.append(val)
        if self.min_index is None:
            self.min_index = 0
        elif val < self.getMin():
            self.min_index = len(self.store) - 1

    def pop(self) -> None:
        _ = self.store.pop()
        if not self.store:
            self.min_index = None
        elif self.min_index >= len(self.store):
            self.min_index = self.store.index(min(self.store))

    def top(self) -> int:
        if self.store:
            return self.store[-1]

    def getMin(self) -> int:
        if self.min_index is not None:
            return self.store[self.min_index]
