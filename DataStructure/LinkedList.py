'''
LinkedList는 Node들의 연결을 나타내는 것이기 때문에 Node를 가장 먼저 정의합니다.

삽입과 삭제 시에 노드들을 적절히 연결하는 연산이 필요하며, LinkedList는 헤더에 대한 정보만을 가지고 있으면 됩니다.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 맨 앞에 삽입
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # 맨 앞 삭제
    def delete_head(self):
        target = self.head
        self.head = self.head.next
        del(target)

    # 특정 인덱스 삽입은 search를 변형해서 작성할 수 있다.

    # serach는 value의 존재 유무만 판단한다.
    def search(self, value):
        pointer = self.head

        while pointer != None:
            if pointer.value == value:
                return 1
            pointer = pointer.next

        return 0

    # 모든 아이템을 연결 관계로 출력.
    def get_all_items(self):
        pointer = self.head

        while pointer != None:
            print(pointer.value, end='->')
            pointer = pointer.next
        print(None)


linkedList = LinkedList()

linkedList.insert_head(1)
linkedList.insert_head(2)
linkedList.insert_head(3)
linkedList.delete_head()
linkedList.insert_head(4)
linkedList.get_all_items()
