SIZE = 1024


class heap:
    def __init__(self):
        self.list = [-1]*SIZE
        self.len = 1

    def push(self, val):
        self.list[self.len] = val
        index = self.len
        self.len += 1

        while index//2:
            if self.list[index] > self.list[index//2]:
                self.list[index], self.list[index //
                                            2] = self.list[index//2], self.list[index]
                index = index//2
            else:
                break

    def pop(self):
        self.list[1], self.list[self.len -
                                1] = self.list[self.len-1], self.list[1]
        value = self.list[self.len]
        self.list[self.len] = -1
        self.len -= 1
        self.heapify()
        return value

    def heapify(self):
        index = 1
        while index*2+1 < self.len:
            if self.list[index*2] > self.list[index*2+1]:
                child = index*2
            else:
                child = index*2+1
            if self.list[index] < self.list[child]:
                self.list[index], self.list[child] = self.list[child], self.list[index]
                index = child
            else:
                break

    def get_all_items(self):
        print(self.list[1:self.len])


h = heap()

h.push(1)
h.push(3)
h.push(4)
h.push(2)
h.push(3)
h.pop()
h.pop()
h.get_all_items()
