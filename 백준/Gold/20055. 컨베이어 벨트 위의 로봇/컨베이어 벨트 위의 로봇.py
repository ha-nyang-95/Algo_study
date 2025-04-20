N, K = map(int, input().split())
belt = []
for j in map(int, input().split()):
    belt.append([j, 0])

# 내구도 0의 개수
zero_num = 0
count = 0
while zero_num < K:
    # 1. 벨트 회전
    new_belt = [[0, 0] for _ in range(2 * N)]
    for i in range(2 * N):
        if i == 2 * N - 1:
            new_belt[0] = belt[i]
        else:
            new_belt[i + 1] = belt[i]
    # 벨트 회전이 끝나고, N-1칸에 로봇이 있다면 제거
    if new_belt[N - 1][1] == 1:
        new_belt[N - 1][1] = 0

    # 2. 로봇 이동
    # 먼저 올라온 순서부터 진행
    # 즉, N-2 부터 시작해야 함!
    # 로봇이 있다면, 다음 칸에 로봇이 있는지 확인 후
    # 없다면 칸의 내구도가 1 이상일 때 움직인다.
    for r in range(N - 2,-1,-1):
        if new_belt[r][1] and not new_belt[r + 1][1] and new_belt[r + 1][0] > 0:
            new_belt[r][1], new_belt[r + 1][1] = new_belt[r + 1][1], new_belt[r][1]
            # new_belt[r][1] = 0
            # new_belt[r + 1][1] = 1
            new_belt[r + 1][0] -= 1
            if not new_belt[r + 1][0]:
                zero_num += 1
            if r + 1 == N - 1:
                new_belt[r + 1][1] = 0

    # 3. 0번 칸이 내구도가 0보다 클 때 그리고 로봇이 없을때,
    #    로봇을 올리고 내구도 -1
    if new_belt[0][0] > 0 and not new_belt[0][1]:
        new_belt[0][1] = 1
        new_belt[0][0] -= 1
        if not new_belt[0][0]:
            zero_num += 1

    belt = new_belt
    count += 1

print(count)