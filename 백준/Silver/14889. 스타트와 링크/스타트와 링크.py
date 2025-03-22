from collections import defaultdict

# 부분집합을 재귀로 생성하며,
# 부분집합을 방문한 적이 있는지,
# 부분집합 개수를 충족했는지를 체크하며
# 시너지의 최소값을 구한다.
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


# 각 부분집합들의 시너지 합을 구하기 위한 함수
def sum_list(li):
    test = 0
    for a in li:
        for b in li:
            if a == b: continue
            test += stat[a][b]
    return test


N = int(input())
stat = [list(map(int, input().split())) for _ in range(N)]
# visited를 통해 한번 방문한 부분집합은 통과하게 만든다.
visited = defaultdict(bool)
result = float('inf')
# 부분집합을 시작할 숫자
for i in range(N):
    dfs([i])
print(result)
