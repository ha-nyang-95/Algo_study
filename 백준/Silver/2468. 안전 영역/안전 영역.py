# import sys
# sys.stdin=open('testcases/1/input.txt')

from collections import deque

def search(p):
    count = 0
    for r in range(N):
        for c in range(N):
            if mountain[r][c] <= p:
                test[r][c] = 0
                continue
            if test[r][c]:
                bfs(r, c, p)
                count += 1
    return count


def bfs(r, c, p):
    queue = deque([(r, c)])
    test[r][c] = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and test[nr][nc]:
                if mountain[nr][nc] <= p:
                    test[nr][nc] = 0
                    continue
                test[nr][nc] = 0
                queue.append((nr, nc))


N = int(input())
mountain = [list(map(int, input().split())) for _ in range(N)]
# 비가 오지 않는 경우도 고려해야 한다.
num = {0}
for line in mountain:
    num.update(line)

result = 0
for i in num:
    test = [[1 for _ in range(N)] for _ in range(N)]
    # 굳이 함수 두개를 작성해야 했을까?
    # 여기서 i 이하인 높이들을 전부 0처리 하고 함수로 넘어갔다면
    # 하나의 함수로 해결가능 할 거 같은데, 시간 차이도 별로 없어보임
    result = max(result, search(i))

print(result)
