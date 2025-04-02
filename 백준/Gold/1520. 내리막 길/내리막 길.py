import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
number_map = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

# DFS + 메모이제이션
def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N:
            if number_map[nr][nc] < number_map[r][c]:
                dp[r][c] += dfs(nr, nc)
    return dp[r][c]

print(dfs(0, 0))