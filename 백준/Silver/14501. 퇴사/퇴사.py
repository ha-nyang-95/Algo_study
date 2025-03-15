from collections import deque


def bfs(cur_p, benefit):
    global result
    # 현위치와 현재 누적 수익을 저장
    queue = deque([(cur_p, benefit)])
    while queue:
        P, V = queue.popleft()
        # 다음 위치의 인덱스와
        # 다음 위치로 이동할 때 가질 수 있는 수익
        np = P + meeting[P][0]
        nv = V + meeting[P][1]
        # 다음 위치가 N보다 크다면 갈 수 없는 위치이기 때문에
        # 현재까지 누적된 수익을 비교
        if np > N:
            result = max(result, V)
            continue
        elif np == N:
            result = max(result, nv)
            continue
        for j in range(np, N):
            queue.append((j, nv))


N = int(input())
# 각 리스트의
# 첫번째 값은 현위치에서 일이 끝나는 시점까지 이동할 숫자
# 두번째 값은 일을 끝냈을 때 받을 수 있는 수익
meeting = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(N):
    if i + meeting[i][0] < N:
        bfs(i, 0)
    elif i + meeting[i][0] == N:
        result = max(result, meeting[i][1])
print(result)
