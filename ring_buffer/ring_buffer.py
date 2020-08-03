class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_index = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.oldest_index] = item
            self.oldest_index += 1
            if self.oldest_index > self.capacity-1:
                self.oldest_index = 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage
