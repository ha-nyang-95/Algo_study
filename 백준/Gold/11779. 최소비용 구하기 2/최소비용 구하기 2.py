import heapq

# 도시의 개수 n과 버스(또는 도로)의 개수 m을 입력받음
n = int(input())
m = int(input())

# 각 도시에서 출발하는 버스 정보를 저장할 리스트를 생성 (1번 도시부터 n번 도시까지 사용)
# city[i]에는 (도착 도시, 이동 비용) 튜플들이 저장됨
city = [[] for _ in range(n + 1)]

# 각 버스 노선에 대한 정보를 입력받아 city 리스트에 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    city[a].append((b, c))

# 시작 도시와 도착 도시를 입력받음
start_P, end_P = map(int, input().split())

# 무한대를 표현할 수 있는 INF 설정
INF = float('inf')
# 시작 도시부터 각 도시까지 도달하는 최소 비용을 저장할 리스트 (처음에는 모두 INF로 초기화)
dist = [INF] * (n + 1)
# 최단 경로를 복원하기 위해 각 도시로 오기 바로 전의 도시 정보를 저장할 리스트
prev = [0] * (n + 1)

# 시작 도시는 비용 0으로 초기화
dist[start_P] = 0

# 우선순위 큐(최소 힙)를 사용하여 (비용, 도시) 튜플을 저장
heap = [(0, start_P)]

# 다익스트라 알고리즘 실행: 시작 도시에서부터 모든 도시까지의 최소 비용을 구함
while heap:
    # 현재까지 비용이 가장 낮은 도시를 꺼냄
    cost, cur = heapq.heappop(heap)

    # 이미 더 적은 비용으로 도달한 경우라면 건너뜀
    if dist[cur] < cost:
        continue

    # 현재 도시에서 이동 가능한 모든 다음 도시들을 확인
    for nxt, w in city[cur]:
        # 현재 도시까지의 비용(cost)에 다음 도시로 이동하는 비용(w)를 더한 값이
        # 지금까지 저장된 nxt 도시까지의 최소 비용보다 작으면 업데이트
        if dist[nxt] > cost + w:
            dist[nxt] = cost + w  # 최소 비용 갱신
            prev[nxt] = cur  # nxt 도시로 오기 전에 cur 도시를 거쳤음을 기록
            heapq.heappush(heap, (dist[nxt], nxt))  # 새로 갱신된 비용과 도시 정보를 힙에 추가

# 최단 경로를 복원하는 과정
path = []
cur = end_P  # 도착 도시부터 경로를 역추적
while cur:
    path.append(cur)  # 현재 도시를 경로에 추가
    cur = prev[cur]  # 이전 도시로 이동 (prev 리스트를 사용하여 역추적)

# 경로가 도착 도시부터 시작 도시 순으로 저장되어 있으므로, 올바른 순서(시작->도착)로 바꾸기 위해 reverse
path.reverse()

# 결과 출력:
# 1. 시작 도시에서 도착 도시까지의 최소 비용
# 2. 최단 경로에 포함된 도시의 수
# 3. 최단 경로에 포함된 도시들의 번호
print(dist[end_P])
print(len(path))
print(*path)