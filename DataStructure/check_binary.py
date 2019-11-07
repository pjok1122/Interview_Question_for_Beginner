'''
주어진 트리가 binary 트리인지 판단하자.

그러기 위해선 트리가 어떠한 형태로 주어졌는지가 중요하다.

인접행렬로 주어진 경우에 대해 구현해보자.

루트는 0으로 가정했으나, 실제에서는 0이 루트가 아닐 수 있다. 이런 경우에는 단말노드를 루트로 설정해주면 해결할 수 있다.

'''

from collections import deque


def check_binary(tree):
    q = deque()
    visited = [0]*len(tree)
    for i, row in enumerate(tree):
        if row.count(1) == 1:
            root = i
            break

    while q:
        node = q.popleft()
        cnt = 0  # 자식 노드의 수
        for i in range(len(tree)):
            if tree[node][i] and not visited[i]:
                visited[i] = 1
                cnt += 1

        if cnt > 2:
            return 0
    return 1
