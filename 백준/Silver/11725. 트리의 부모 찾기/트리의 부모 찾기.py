from collections import deque


def bfs(a):
    queue = deque([a])

    while queue:
        a = queue.popleft()
        for b in connected[a]:
            if parent[b] == -1:
                parent[b] = a
                queue.append(b)


N = int(input())
connected = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]
# visited
for _ in range(N - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
parent[1] = 0
bfs(1)
for i in range(2, N + 1):
    print(parent[i])
