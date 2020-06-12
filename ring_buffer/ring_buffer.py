class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.add = 0

    def append(self, item):
        if self.add <= (self.capacity - 1):
            self.data.insert(self.add, item)
            self.add += 1
            
        else:
            index = self.add % self.capacity
            self.add += 1
            self.data[index] = item

    def get(self):
        return self.data