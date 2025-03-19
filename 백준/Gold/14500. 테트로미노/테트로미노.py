from itertools import combinations

# 4 방향
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 끊어진 경우를 제외하고 모든 경우의 수를 충족할 함수
def first_find(r, c, dep, total):
    global result

    # 4칸을 모두 이동한 경우 최대값 반환
    if dep == 4:
        result = max(result, total)
        return

    # 재귀함수를 통해 4방향을 이동해
    # 그 지점에서 또 4방향을 이동하는 것을 반복하며
    # 4번의 이동을 충족한다.
    # 그러면, 끊어진 경우를 제외하고는 모든 도형이 만들어진다.
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            first_find(nr, nc, dep + 1, total + tetris[nr][nc])
            visited[nr][nc] = False


# ㅗ,ㅓ,ㅏ,ㅜ 와 같이 가운데로 이동하면 더이상 이동할 수 없는
# 경우는 따로 함수를 만들어 계산
def second_find(r, c):
    global result
    test = tetris[r][c]
    cross = []
    # 끊어진 경우를 탐색하기 위해
    # 4방향 중 갈 수 있는 곳을 리스트에 저장한다.
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            cross.append(tetris[nr][nc])

    # 적어도 3방향으로 이동할 수 있어야 정사각형 4개의 테트로미노가 만들어지기 때문에
    # 리스트에 3개 미만으로 있다면 함수를 탈출한다.
    if len(cross) < 3:
        return

    # [기준점 + 세 개의 지점]을 해줘야 하기 때문에,
    # cross 리스트 안에 있는 숫자로 3개짜리 부분집합을 만들어준다.
    for cross_set in combinations(cross, 3):
        result = max(result, test + sum(cross_set))


# N 세로 / M 가로
N, M = map(int, input().split())
# 점수맵
tetris = [list(map(int, input().split())) for _ in range(N)]
# 왔던 방향을 가지 않기 위한 방문 변수
visited = [[False for _ in range(M)] for _ in range(N)]
# 최대값을 저장하기 위한 변수
result = 0

# 모든 칸을 탐색
# 백트래킹을 통해 모든 칸을 이동할 때 visited 변수를 초기화한다.
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        first_find(i, j, 1, tetris[i][j])
        visited[i][j] = False

        second_find(i, j)

print(result)
