class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.index = 0
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            if self.ignore_case:
                item = item.lower()
            if self.index == 0 or self.items[self.index - 1] != item:
                self.index += 1
                return item
            self.index += 1
        raise StopIteration

    def __iter__(self):
        return self