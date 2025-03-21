from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
queue=deque([])
result = 0

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, result))

while queue:
    r, c, result = queue.popleft()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not box[nr][nc]:
            box[nr][nc] = 1
            queue.append((nr, nc, result + 1))

for line in box:
    if 0 in line:
        print(-1)
        break
else:
    print(result)