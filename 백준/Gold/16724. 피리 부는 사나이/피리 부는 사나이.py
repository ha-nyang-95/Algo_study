# from collections import deque
#
# dir = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
#
#
# def Zone(r, c):
#     queue = deque([(r, c, farm[r][c])])
#     visited[r][c] = True
#
#     while queue:
#         # test = 'D'
#         test_r, test_c, direction = queue.popleft()
#         dr, dc = dir[direction]
#         nr, nc = test_r + dr, test_c + dc
#         if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
#             queue.append((nr, nc, farm[nr][nc]))
#             visited[nr][nc] = True
#
#
# M, N = map(int, input().split())
# farm = [list(input()) for _ in range(M)]
# visited = [[False] * N for _ in range(M)]
# flag = True
# count = 0
# for r in range(M):
#     for c in range(N):
#         if not visited[r][c]:
#             Zone(r, c)
#             count += 1
#
# print(count)


import sys

sys.setrecursionlimit(10 ** 6)

# 방향 매핑 (각 칸은 단 하나의 방향을 가짐)
dir_map = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}


def follow_chain(r, c, group_id):
    """
    (r, c)에서 출발하여 체인을 따라가면서 현재 경로(path)를 기록.
    만약 체인 중에 현재 경로에 이미 포함된 칸을 만나면 사이클이 발견된 것으로 판단.
    체인 종료 후, 현재 경로에 포함된 모든 칸의 visited 값을 group_id로 업데이트.
    사이클이 발견되면 True를 반환하고, 아니라면 False를 반환.
    """
    path = []  # 현재 체인에 있는 좌표를 순서대로 저장
    cur_r, cur_c = r, c
    cycle_found = False

    while True:
        # 만약 현재 칸이 이미 처리된(방문된) 상태라면 체인 종료
        if visited[cur_r][cur_c] != 0:
            # 만약 현재 칸이 현재 경로에 이미 포함되어 있었다면 사이클 발생
            if (cur_r, cur_c) in path:
                cycle_found = True
            else:
                group_id = visited[cur_r][cur_c]
            break

        # 현재 칸을 “처리 중”(임시 마킹: -1)으로 표시하고 경로에 추가
        visited[cur_r][cur_c] = -1
        path.append((cur_r, cur_c))
        dx, dy = dir_map[farm[cur_r][cur_c]]
        cur_r, cur_c = cur_r + dx, cur_c + dy

    # 현재 체인(path)에 속한 아직 -1로 남아있는(처리 중) 칸들을 group_id로 업데이트
    for pr, pc in path:
        if visited[pr][pc] == -1:
            visited[pr][pc] = group_id
    return cycle_found


# 입력 처리
M, N = map(int, input().split())
farm = [list(input().strip()) for _ in range(M)]
# visited 배열: 0은 미방문, -1은 현재 체인에서 처리 중, 양의 정수는 그룹(안전 영역) 번호
visited = [[0] * N for _ in range(M)]
safe_zone_count = 0

for r in range(M):
    for c in range(N):
        if visited[r][c] == 0:  # 아직 처리되지 않은 칸이면
            if follow_chain(r, c, safe_zone_count + 1):
                safe_zone_count += 1

print(safe_zone_count)
# for i in range(M):
#     print(visited[i])
