from collections import deque

N, M = map(int, input().split())
relations = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

min_total = float('inf')
result = 0

for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    queue = deque()
    queue.append(i)
    visited[i] = 0  # 자기 자신은 거리 0

    while queue:
        cur = queue.popleft()
        for neighbor in relations[cur]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[cur] + 1
                queue.append(neighbor)
    total= sum(visited[1:])
    if total < min_total:
        min_total = total
        result = i

print(result)