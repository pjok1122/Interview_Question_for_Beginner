'''
tree를 다음과 같이 정의해두면 순회가 편하다.
tree[x][0] : x의 왼쪽 자식노드
tree[x][1] : x의 오른쪽 자식노드
자식이 없는 경우, -1을 저장한다고 하자.
'''


def pre_order(tree, x):
    if x == -1:
        return
    print(x, end=' ')  # 루트 방문
    pre_order(tree, tree[x][0])
    pre_order(tree, tree[x][1])


def in_order(tree, x):
    if x == -1:
        return
    pre_order(tree, tree[x][0])
    print(x, end=' ')  # 루트 방문
    pre_order(tree, tree[x][1])


def post_order(tree, x):
    if x == -1:
        return
    pre_order(tree, tree[x][0])
    pre_order(tree, tree[x][1])
    print(x, end=' ')  # 루트 방문
