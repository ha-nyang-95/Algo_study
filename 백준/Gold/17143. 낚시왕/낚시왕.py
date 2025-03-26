# 방향: None, 위(1), 아래(2), 오른쪽(3), 왼쪽(4)
dir = [None, (-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, M = map(int, input().split())
shark = [[]] + [list(map(int, input().split())) for _ in range(M)]

Sea = [[0 for _ in range(C)] for _ in range(R)]

# 상어 초기 배치: 가장 큰 상어만 남기고 저장
for i in range(1, M + 1):
    r, c = shark[i][0] - 1, shark[i][1] - 1
    if Sea[r][c]:
        if shark[Sea[r][c]][4] > shark[i][4]:
            continue
        else:
            Sea[r][c] = i
    else:
        Sea[r][c] = i

# 헌터의 위치
hunter_king = -1
# 헌터가 잡은 상어의 총 크기
hunting_shark = 0

# 헌터가 오른쪽 끝에 도달할 때까지 반복
# [상어가 사라지는 경우]
# 1. 헌터가 잡는 경우
# 2. 서로 잡아먹는 경우
# shark 리스트에서 상어의 정보를 삭제해줘야하고,
# Sea에서 상어를 삭제해줘야한다.
while hunter_king != C - 1:
    hunter_king += 1

    # 1. 헌터가 가장 가까운 상어를 잡는다
    for i in range(R):
        if Sea[i][hunter_king]:
            idx = Sea[i][hunter_king]
            hunting_shark += shark[idx][4]
            shark[idx] = []  # 잡힌 상어는 삭제
            Sea[i][hunter_king] = 0
            break

    # 2. 상어 이동
    new_Sea = [[0 for _ in range(C)] for _ in range(R)]  # 이동 후의 Sea

    for i in range(1, M + 1):
        if not shark[i]:  # 이미 잡혔거나 먹힌 상어는 생략
            continue

        r, c, s, d, z = shark[i]
        r -= 1  # 0-index
        c -= 1

        dr, dc = dir[d]

        # 속도 최적화: 원형 반복(방향도 일치한 상태로 원위치로 돌아오는 경우)을 피하기 위해 나머지 계산
        if d in [1, 2]:  # 상하
            s %= (R - 1) * 2
        else:  # 좌우
            s %= (C - 1) * 2
    
        # 방향에 따라 이동 처리
        for _ in range(s):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R):
                dr *= -1
                d = 2 if d == 1 else 1  # 위<->아래
                nr = r + dr
            if not (0 <= nc < C):
                dc *= -1
                d = 4 if d == 3 else 3  # 오<->왼
                nc = c + dc
            r, c = nr, nc

        # 이동 후 좌표와 방향을 업데이트
        shark[i] = [r + 1, c + 1, s, d, z]

        # 같은 위치에 상어가 있으면 크기 비교
        if new_Sea[r][c]:
            exist_idx = new_Sea[r][c]
            if shark[exist_idx][4] > z:
                shark[i] = []  # 내가 잡아먹힘
            else:
                shark[exist_idx] = []  # 상대방이 잡아먹힘
                new_Sea[r][c] = i
        else:
            new_Sea[r][c] = i

    # 새로운 Sea로 갱신
    # 여기까지가 바다를 갱신하기 위해
    # 헌터가 한칸 움직이고, 상어들이 움직인 현재 정보다.
    Sea = new_Sea

print(hunting_shark)
