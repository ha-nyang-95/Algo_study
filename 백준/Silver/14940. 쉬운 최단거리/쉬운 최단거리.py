from collections import deque

n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    flag = False
    for j in range(m):
        if land[i][j] == 2:
            flag = True
            r, c = i, j
            break
    if flag:
        break

distance[r][c] = 0
queue = deque([(r, c)])
while queue:
    r, c = queue.popleft()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1 and distance[nr][nc] == -1:
            queue.append((nr, nc))
            distance[nr][nc] = distance[r][c] + 1

for a in range(n):
    for b in range(m):
        if land[a][b] == 0:
            print(0, end=' ')
        else:
            print(distance[a][b], end=' ')
    print()
