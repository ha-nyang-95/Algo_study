from collections import deque

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    map_ = [list(map(int, input())) for _ in range(N)]
    memo = [[float('inf') for _ in range(N)] for _ in range(N)]

    q = deque([(0, 0)])
    memo[0][0] = 0
    # memo에는 누적값을 저장한다.
    # 그 위치까지 최초의 도착한 경로에 대한 누적값을 입력하고
    # 이후 도착했을 때 그 누적값보다 작은 값이 있다면, 갱신한다.

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if memo[nr][nc] > memo[r][c] + map_[nr][nc]:
                memo[nr][nc] = memo[r][c] + map_[nr][nc]
                q.append((nr, nc))

    print(f'#{tc} {memo[N - 1][N - 1]}')