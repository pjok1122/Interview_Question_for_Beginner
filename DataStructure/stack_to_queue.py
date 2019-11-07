class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop(-1))

        if len(self.stack2) > 0:
            return self.stack2.pop(-1)
        else:
            return None


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
q.push(4)
q.push(5)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
