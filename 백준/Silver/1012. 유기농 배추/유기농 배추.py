def dfs(i, j):
    stack = [(i, j)]

    while stack:
        r, c = stack.pop()
        farm[r][c] = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and farm[nr][nc]:
                stack.append((nr, nc))


for tc in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                dfs(i, j)
                count += 1

    print(count)
