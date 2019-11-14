'''
1. 탐색 연산 : head부터 원하는 값이 있는지 탐색해 나간다.
2. 삽입 연산 : head가 None인 경우와 아닌 경우로 나눈다. head가 None이 아닌 경우는 head부터 내려가는 데, parent 정보를 유지하고 있다가 조건을 만족하는 위치에 삽입한다.
3. 삭제 연산
  1) 삭제하고자 하는 노드가 단말노드인 경우
  2) 삭제하고자 하는 노드가 한 쪽의 자식노드를 갖는 경우
  3) 삭제하고자 하는 노드가 양 쪽의 자식노드를 모두 갖는 경우


'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        if root != None:
            print(root.val, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def search(self, val):
        pointer = self.root

        while pointer != None:
            if pointer.val == val:
                return 1
            elif pointer.val < val:
                pointer = pointer.right
            elif pointer.val > val:
                pointer = pointer.left
        return 0

    def insert(self, val):
        parent = self.root
        child = self.root
        node = Node(val)

        if parent == None:
            self.root = node
            return True

        while child != None:
            parent = child
            if child.val == val:
                return False
            elif child.val < val:
                child = child.right
            elif child.val > val:
                child = child.left

        if parent.val < val:
            parent.right = node
        elif parent.val > val:
            parent.left = node
        return True

    def delete(self, val):
        parent = self.root
        child = self.root

        while child.val != val:
            parent = child

            if child.val < val:
                child = child.right
            else:
                child = child.left

        # 자식이 없는 경우,
        if child.left == child.right == None:
            if parent.val > child.val:
                parent.left = None
            else:
                parent.right = None
            del(child)

        # 1개의 자식만을 갖는 경우,
        elif child.left == None or child.right == None:
            new_child = child.left if child.left != None else child.right
            if parent.val > child.val:
                parent.left = new_child
            else:
                parent.right = new_child
            del(child)

        # 2개의 자식을 갖는 경우, (왼쪽 서브 트리의 가장 큰 값이나 오른쪽 서브 트리의 가장 작은 값을 child 자리로 바꿔준다.)
        else:
            pa = None
            ch = child.left
            while ch.right != None:
                pa = ch
                ch = ch.right

            if pa != None:
                pa.right = ch.left
                child.val = ch.val
            else:
                child.left = ch.left
                child.val = ch.val
            del(ch)


bst = BinarySearchTree()
bst.insert(7)
bst.insert(6)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.delete(2)
bst.pre_order(bst.root)
