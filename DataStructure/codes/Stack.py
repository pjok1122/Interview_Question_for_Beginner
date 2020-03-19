'''
Array : 삽입,삭제 O(1), 초기 크기 설정의 단점 존재.
List  : 삽입,삭제 O(1), 초기 크기 설정의 단점 X.
LinkedList : 삽입,삭제 O(1), 초기 크기 설정의 단점 X, 별도의 저장공간 필요. 

따라서 스택은 시간복잡도 측면에선 어떤 방법으로 구현해도 상관없으나, 사용하는 입장에서는 Array나 List 타입으로 구현하는 것이 가장 좋다. 
'''

# Array로 구현한 스택 (사이즈가 미리 정해진다.)
SIZE = 1024


class Stack:
    def __init__(self):
        self.arr = [0]*SIZE
        self.top = -1

    def push(self, val):
        if(self.top > SIZE - 2):
            return None
        self.top += 1
        self.arr[self.top] = val

    def is_empty(self):
        if self.top == -1:
            return 1
        else:
            return 0

    def pop(self):
        if not self.is_empty():
            val = self.arr[self.top]
            self.top -= 1
            return val
        else:
            return None


s = Stack()
s.push(1)
s.push(2)
print(s.pop())
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())

# List를 이용한 Stack


class Stack2:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def is_empty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0

    def pop(self):
        if not self.is_empty():
            return self.list.pop(-1)
        else:
            return None


s = Stack2()
s.push(1)
s.push(2)
print(s.pop())
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())

# LinkedList를 이용한 Stack


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack3:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head == None:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val


s = Stack3()
s.push(1)
s.push(2)
print(s.pop())
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
