'''
토마토가 모두 익는 최소 날짜수를 구해야 한다.
이때, 토마토가 들어있지 않아 모든 토마토가 익지 못하는 경우가 생길 수 있기 때문에
최종적으로 모든 토마토가 익었는지 확인하는 작업이 필요하다.
'''

from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
queue=deque([])
result = 0

# 익은 토마토가 들어있는 상자부터 인접한 익지 않은 토마토를 익게 만들어줘야 한다.
# 그러므로 익어있는 토마토의 위치를 탐색하고, 며칠이 지난 것인지에 대한 수를 세는 변수를 입력한다.
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j, result))

# 큐가 빌때까지 인접한 곳으로 토마토를 익히는 작업을 반복한다.
# 익은 토마토의 인접한 부분이 익지 않은 토마토인 경우에만 큐에 저장하며
# 이때, 며칠이 지났는지 알 수 있기 위해 하루씩 추가한다.
# 최종적으로 큐의 마지막 요소를 실행할 때 큐가 비며 최종 날을 result라는 변수를 통해 알 수 있다.
while queue:
    r, c, result = queue.popleft()
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not box[nr][nc]:
            box[nr][nc] = 1
            queue.append((nr, nc, result + 1))

# 토마토를 익히는 작업이 모두 완료되었기 때문에,
# 모든 칸에 익지않은 토마토가 존재하는지를 검토해준다.
for line in box:
    if 0 in line:
        print(-1)
        break
else:
    print(result)
