class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            self.items = []
        else:
            self.items = items

        self.limit = limit

    def push(self, value):
        # If there's a limit and we're full, ignore the push
        if self.limit is not None and len(self.items) >= self.limit:
           return self
        self.items.append(value)
        return self

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        for i in range(len(self.items)-1, -1, -1):
            if self.items[i] == value:
                return len(self.items) - 1 - i
        return -1
