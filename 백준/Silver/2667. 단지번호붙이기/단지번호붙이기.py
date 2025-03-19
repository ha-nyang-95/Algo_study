from collections import deque


def bfs(r, c):
    count = 1
    queue = deque([(r, c)])
    home_map[r][c] = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and home_map[nr][nc]:
                home_map[nr][nc] = 0
                queue.append((nr, nc))
                count += 1
    area.append(count)


N = int(input())
home_map = [list(int(a) for a in input()) for _ in range(N)]
result = 0
area = []
for i in range(N):
    for j in range(N):
        if home_map[i][j] == 1:
            bfs(i, j)
            result += 1
area.sort()
print(result)
for b in area:
    print(b)
