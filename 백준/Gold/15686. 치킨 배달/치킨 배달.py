'''
0은 빈칸 / 1은 집 / 2는 치킨집
최대 이득을 볼 수 있는 치킨집의 개수를 구해야한다.
최대 이득이란 각 집에서 치킨 거리가 최소값이 되는 값들의 합이 가장 작아야한다.
그렇다면, 1인 집들의 위치를 모두 모으고,
치킨집들의 위치를 모두 모아
각 집의 위치에서 치킨집들과의 거리를 비교해 최소값을 누적으로 더해주는 변수를 만들고,
치킨집의 개수가 3개라면,
3개를 가진 부분집합
2개를 가진 부분집합
1개를 가진 부분집합들을 전부 반복한 다음
가장 작은 치킨 거리를 구해주면 가능할까?

더 빨리 구하기 위해서는?
메모이제이션?
집의 위치와 치킨 집의 위치의 거리를 먼저 구해서
집의 위치, 치킨 집의 위치 : 거리
위의 형식으로 딕셔너리로 저장하면서
딕셔너리에 없는 값들만 저장하면 처음 반복문을 돌 때
계산했던 값들을 재활용할 수 있지 않을까?
'''

from itertools import combinations
from collections import defaultdict

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 위치 저장
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
# [((1, 2), (2, 2), (4, 4)),
#  ((1, 2), (2, 2)), ((1, 2), (4, 4)), ((2, 2), (4, 4)),
#  ((1, 2),), ((2, 2),), ((4, 4),)]
chicken_subsets = []
for c in range(M, 0, -1):
    chicken_subsets += list(combinations(chicken, c))

# 그럼 defaultdict에는 어떤 값들을 저장?
# 집의 위치를 key로, (거리, 치킨집의 위치)를 리스트로 저장해서
# 거리를 가중치로 정렬시키면 되지 않을까?
# 정렬 후에 defaultdict를 어떻게 사용할 것인가?
# -> 각 집의 리스트를 불러와 첫번째 부터 a,b,c로 값을 불러와
# -> 부분집합안에 (b,c)가 있는지 확인 후 확인이 되면
# -> 그 값이 최소값이니 누적합에 a를 더해주고 다음 집으로 넘어가면 될 거 같은데?
# {(0, 2): [(1, 1, 2), (2, 2, 2), (6, 4, 4)],
#  (1, 4): [(2, 1, 2), (3, 2, 2), (3, 4, 4)],
#  (2, 1): [(1, 2, 2), (2, 1, 2), (5, 4, 4)],
#  (3, 2): [(1, 2, 2), (2, 1, 2), (3, 4, 4)]}
distance = defaultdict(list)
for r, c in home:
    for a, b in chicken:
        distance[(r, c)] += [(abs(r - a) + abs(c - b), a, b)]
for key, value in distance.items():
    value.sort(key=lambda x: x[0])

result = float('inf')
for chicken_subset in chicken_subsets:
    test = 0
    for r, c in home:
        for v, a, b in distance[(r, c)]:
            if (a, b) in chicken_subset:
                test += v
                break
        if test >= result:
            break
    else:
        result = test

# 출력: 5
print(result)