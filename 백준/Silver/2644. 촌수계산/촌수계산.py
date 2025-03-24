from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
relations = [None] + [[] for _ in range(n)]
for _ in range(m):
    c, d = map(int, input().split())
    relations[c].append(d)
    relations[d].append(c)
visited = [False for _ in range(n + 1)]
result = 0
queue = deque([(a, 0)])
visited[a] = True
while queue:
    t, c = queue.popleft()
    for i in relations[t]:
        if i == b:
            result = c + 1
            break
        if not visited[i]:
            queue.append((i, c + 1))
            visited[i] = True
    else:
        continue
    break
if not result:
    print(-1)
else:
    print(result)