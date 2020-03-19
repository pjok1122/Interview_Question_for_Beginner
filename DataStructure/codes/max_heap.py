SIZE = 1024


class heap:
    def __init__(self):
        self.list = [-1]*SIZE
        self.len = 0

    def push(self, val):
        self.len += 1
        self.list[self.len] = val
        index = self.len

        while index//2:
            if self.list[index] > self.list[index//2]:
                self.list[index], self.list[index //
                                            2] = self.list[index//2], self.list[index]
                index = index//2
            else:
                break

    def pop(self):
        value = self.list[1]
        self.list[1] = self.list[self.len]
        self.list[self.len] = -1
        self.len -= 1
        self.heapify()
        return value

    def heapify(self):
        max_pos = 1
        max_val = self.list[1]
        parent = 1

        while 2*parent <= self.len:
            left_child = 2*parent
            right_child = 2*parent + 1

            if(left_child <= self.len and max_val < self.list[left_child]):
                max_pos = left_child
                max_val = self.list[left_child]

            if(right_child <= self.len and max_val < self.list[right_child]):
                max_pos = right_child
                max_val = self.list[right_child]

            if(parent == max_pos):
                break

            self.list[max_pos] = self.list[parent]
            self.list[parent] = max_val
            parent = max_pos

    def get_all_items(self):
        print(self.list[1:self.len+1])


h = heap()

h.push(-8)
h.push(-2)
h.push(-5)
h.push(-3)
h.push(-1)
h.get_all_items()
print(h.pop())
# h.get_all_items()
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
# print(h.pop())
