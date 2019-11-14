from collections import deque


class Node:
    def __init__(self, key, string=None):
        self.key = key
        self.string = string
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        # 마지막 노드에는 최종 문자열도 삽입
        curr_node.string = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[char]

        if curr_node.string != None:
            return True

    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        q = deque()

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return None
        q.append(curr_node)
        while q:
            curr_node = q.popleft()
            if curr_node.string:
                result.append(curr_node.string)
            for child in list(curr_node.children.values()):
                q.append(child)

        return result


trie = Trie()
trie.insert('joe')
trie.insert('john')
trie.insert('johnny')
trie.insert('jane')
trie.insert('jack')
print(trie.search('jack'))
print(trie.search('jaek'))
print(trie.starts_with('jo'))
