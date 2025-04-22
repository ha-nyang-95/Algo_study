'''
구슬은 N번만 쏘기 가능
가로 W / 세로 H
1. 처음 구술은 항상 맨 위의 벽돌만 깨트릴 수 있다.
2. 구슬을 명중한 벽돌에 적힌 숫자-1만큼 상하좌우의 벽돌을 깨뜨린다.
2-1. 이때, 범위안에 깨진 벽돌 또한 숫자를 파악후 그 숫자만큼
     상하좌우로 또 벽돌을 깬다.
3. 벽돌의 밑으로 빈공간이 생기면, 벽돌을 밑으로 이동시켜준다.

남은 벽돌의 최소 개수를 구해라.
'''
from collections import deque
import copy

T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    brick_map = [list(map(int, input().split())) for _ in range(H)]

    # 큐를 쓸거다.
    # 1. 벽돌을 깨부수는 것만 생각하자.
    #    가로의 모든 칸에서 시작하는 경우를 생각해야 한다.
    #    이때, 처음만이 아닌 매번 W만큼의 시작 위치가 생긴다는 것을 인지해야 한다.
    #    그렇다면, 매번 어떤 위치에서 벽돌을 부수기 위해,
    #    새로운 배열판 필요
    # 1. 가로의 맨 위의 칸의 존재하는 벽돌의 위치를 저장
    # 2. 이후, 범위의 벽돌을 전부 깬다
    # 3. 각 벽돌을 제일 밑으로 내려준다.
    # 한번 돌때마다 횟수를 한번씩 사용
    q = deque()
    q.append([brick_map, N])
    result = float('inf')
    while q:
        cur_map, cnt = q.popleft()
        # 횟수를 다 썼을 때 종료
        if not cnt:
            test = 0
            for r in range(H):
                for c in range(W):
                    if cur_map[r][c]:
                        test += 1
            if test < result:
                result = test
            continue

        # 모든 블록이 다 깨졌을 때 종료
        if not sum(map(sum, cur_map)):
            result = 0
            break

        # 한 줄에서 시작할 수 있는 위치 탐색
        for c in range(W):
            for r in range(H):
                if cur_map[r][c]:
                    test_map = copy.deepcopy(cur_map)
                    q2 = deque()
                    q2.append((r, c))
                    # 이제 이 위치에서 깰 수 있는 벽돌을 깬 다음
                    # 벽돌을 정렬 후 그 행렬과 cnt-1을 q에 저장
                    while q2:
                        cur_r, cur_c = q2.popleft()

                        # 범위안에 있는 벽돌들을 추가
                        for i in range(1, test_map[cur_r][cur_c]):
                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                nr, nc = cur_r + dr * i, cur_c + dc * i
                                if not (0 <= nr < H and 0 <= nc < W):
                                    continue
                                if not test_map[nr][nc]:
                                    continue
                                q2.append((nr, nc))

                        # 다음 벽돌로 넘어가기 전에 기존 위치의 벽돌 값을 0으로 입력
                        test_map[cur_r][cur_c] = 0

                    # 벽돌을 깰 수 있는 것들을 전부 깬 후
                    # 행렬을 정렬시켜줘야 한다.
                    for cc in range(W):
                        idx = H - 1
                        for rr in range(H - 1, -1, -1):
                            if test_map[rr][cc]:
                                if not idx == rr:
                                    test_map[rr][cc], test_map[idx][cc] = test_map[idx][cc], test_map[rr][cc]
                                idx -= 1

                    q.append([test_map, cnt - 1])
                    break

    print(f'#{tc} {result}')