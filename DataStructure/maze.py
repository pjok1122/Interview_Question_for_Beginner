'''
미로 찾기

1은 갈 수 있는 길, 0은 벽을 의미한다. (0,0)에서 (n-1,m-1)에 도착할 수 있으면 1을 반환한다.

4 6
1 0 1 1 1 0
1 0 1 0 1 1
1 0 1 0 1 0
1 1 1 0 1 1

4 4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 0

'''

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def DFS_iterative():
    x, y = 0, 0
    stack = []
    visited = [[0 for col in range(m)] for row in range(n)]
    stack.append((x, y))
    while len(stack):
        if (x, y) == (n-1, m-1):
            return 1
        elif y-1 >= 0 and arr[x][y-1] == 1 and not visited[x][y-1]:
            stack.append((x, y))
            y = y-1
            visited[x][y] = 1
        elif y+1 < m and arr[x][y+1] == 1 and not visited[x][y+1]:
            stack.append((x, y))
            y = y+1
            visited[x][y] = 1
        elif x-1 >= 0 and arr[x-1][y] == 1 and not visited[x-1][y]:
            stack.append((x, y))
            x = x-1
            visited[x][y] = 1
        elif x+1 < n and arr[x+1][y] == 1 and not visited[x+1][y]:
            stack.append((x, y))
            x = x+1
            visited[x][y] = 1
        else:
            x, y = stack.pop(-1)
    return 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for col in range(m)] for row in range(n)]
finish = 0


def DFS_recursive(x, y):
    global finish

    if finish:
        return 1
    if (x, y) == (n-1, m-1):
        finish = 1

    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
            DFS_recursive(nx, ny)


print(DFS_iterative())
DFS_recursive(0, 0)
result = finish
print(result)
