from collections import deque

N, M = map(int, input().split())
mirro = [list(input()) for _ in range(N)]

# 방문 체크: visited[r][c][key_mask]
visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]

# 시작점 찾기
for i in range(N):
    for j in range(M):
        if mirro[i][j] == '0':
            start_r, start_c = i, j
            break

q = deque()
q.append((start_r, start_c, 0, 0))  # r, c, key_mask, distance
visited[start_r][start_c][0] = True

while q:
    r, c, keys, count = q.popleft()

    if mirro[r][c] == '1':
        print(count)
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        cell = mirro[nr][nc]
        new_keys = keys

        if cell == '#':
            continue
        if 'a' <= cell <= 'f':
            new_keys |= (1 << (ord(cell) - ord('a')))
        if 'A' <= cell <= 'F':
            if not (new_keys & (1 << (ord(cell) - ord('A')))):
                continue

        if not visited[nr][nc][new_keys]:
            visited[nr][nc][new_keys] = True
            q.append((nr, nc, new_keys, count + 1))
else:
    print(-1)