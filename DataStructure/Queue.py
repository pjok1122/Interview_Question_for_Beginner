'''
Queue를 구현할 때 기억해둘 것은, 삽입 위치를 알려주는 rear와 삭제 위치를 알려주는 front를 이용한다는 사실이다!

Array : 삽입, 삭제 O(1) , 최대 크기가 정해지며, 공간을 재사용하지 못하는 단점이 존재. -->원형 큐로 개선가능하나, 최대 크기가 정해지는 단점이 여전히 남아있음.
List  : 삽입 O(1), 삭제 O(n), 최대 크기 제한이 없음. 구현이 간단함.
LinkedList : 삽입 O(n), 삭제 O(1), 최대 크기 제한이 없음. --> 삽입의 시간복잡도는 tail에 대한 정보를 저장해 둠으로써 개선이 가능하다.
개선된 LinkedList : 삽입 O(1), 삭제 O(1), 최대 크기 제한 없음.

따라서 큐는 시간복잡도 측면에서는 Array나 양방향 연결리스트가 제일 좋다.

'''
SIZE = 1024


class Queue:  # Array로 구현한 큐
    def __init__(self):
        self.arr = [0]*SIZE
        self.front = -1
        self.rear = -1

    def push(self, val):
        if self.rear+1 < SIZE:
            self.rear = self.rear + 1
            self.arr[self.rear] = val
            return True
        else:
            return False

    def pop(self):
        if self.front == self.rear:
            return None

        self.front += 1
        val = self.arr[self.front]
        self.arr[self.front] = None

        return val


class circularQueue:  # 메모리 재사용을 할 수 있는 원형 큐
    # 공백과  포화 상태를 구분짓기 위해 한 칸을 비워둔다.
    def __init__(self):
        self.arr = [0]*SIZE
        self.front = 0
        self.rear = 0

    # (rear+1)%SIZE == front가 되면 Full 상태.
    def push(self, val):
        if (self.rear+1) % SIZE == self.front:
            return False

        self.rear = (self.rear+1) % SIZE
        self.arr[self.rear] = val
        return True

    def pop(self):
        if self.rear == self.front:
            return None
        else:
            self.front = self.front+1
            return self.arr[self.front]


class Queue2:  # List로 구현한 큐
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop(0)


class Node:
    def __init__(self):
        self.val = val
        self.next = None


class Queue3:  # linkedList로 구현한 큐
    def __init__(self):
        self.head = None

    def push(self, val):        # O(n)
        new_node = Node(val)
        pointer = self.head

        if pointer == None:
            self.head = new_node

        else:
            while pointer.next != None:
                pointer = pointer.next

        pointer.next = new_node

    def pop(self):  # O(1)
        node = self.head
        self.head = self.head.next
        val = node.val
        del(node)
        return val


class Queue4:  # 개선된 연결 리스트 큐
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):        # O(n)
        new_node = Node(val)
        pointer = self.tail
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node

    def pop(self):  # O(1)
        node = self.head
        self.head = self.head.next
        val = node.val
        del(node)
        return val
