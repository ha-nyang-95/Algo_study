from collections import deque

N, M = map(int, input().split())
block_map = [list(map(int, input())) for _ in range(N)]

# visited[r][c][0]: 벽 안부순 상태, visited[r][c][1]: 벽 부순 상태
# 각 열과 행의 위치의 0번째 value는 벽을 부수지 않고 방문한 적이 있는지 나타내는 값이다.
# 각 열과 행의 위치의 1번째 value는 벽을 부수고 방문한 적이 있는지 나타내는 값이다.
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

# r, c, 벽부쉈는지 여부, 현재 거리
q = deque()
# (r,c,벽을 부쉈는지의 인덱스 값, 현재까지 이동 칸 수)
q.append((0, 0, 0, 1))  # 시작점에서 벽 안 부순 상태, 거리 1
visited[0][0][0] = True

while q:
    r, c, broken, dist = q.popleft()

    if r == N - 1 and c == M - 1:
        print(dist)
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        # 벽이 아닌 경우
        # 벽을 부슨 유무와 상관없이 block_map이 0이고, 방문한 적이 없다면
        # 이동 가능
        if not block_map[nr][nc] and not visited[nr][nc][broken]:
            visited[nr][nc][broken] = True
            q.append((nr, nc, broken, dist + 1))

        # block_map이 1인데, 아직 부순 경우가 없고 방문하지도 않았을 때,
        # 벽을 부슨 visited로 넘어가 방문을 check
        elif block_map[nr][nc] and not broken and not visited[nr][nc][1]:
            visited[nr][nc][1] = True
            q.append((nr, nc, 1, dist + 1))
else:
    print(-1)