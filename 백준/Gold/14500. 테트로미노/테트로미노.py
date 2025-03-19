from itertools import combinations

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def first_find(r, c, dep, total):
    global result

    if dep == 4:
        result = max(result, total)
        return

    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            first_find(nr, nc, dep + 1, total + tetris[nr][nc])
            visited[nr][nc] = False


def second_find(r, c):
    global result
    test = tetris[r][c]
    cross = []
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            cross.append(tetris[nr][nc])

    if len(cross) < 3:
        return

    for cross_set in combinations(cross, 3):
        result = max(result, test + sum(cross_set))


N, M = map(int, input().split())
tetris = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        first_find(i, j, 1, tetris[i][j])
        visited[i][j] = False

        second_find(i, j)

print(result)