from collections import defaultdict


def dfs(line):
    global result
    if visited[tuple(line)]:
        return
    if len(line) == N // 2:
        line_another = list(set(range(N)) - set(line))
        result = min(result, abs(sum_list(line) - sum_list(line_another)))
        visited[tuple(line)] = True
        visited[tuple(line_another)] = True
        return

    for t in range(line[-1] + 1, N):
        dfs(line + [t])


def sum_list(li):
    test = 0
    for a in li:
        for b in li:
            if a == b: continue
            test += stat[a][b]
    return test


N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
visited = defaultdict(bool)
result = float('inf')
for i in range(N):
    dfs([i])
print(result)
