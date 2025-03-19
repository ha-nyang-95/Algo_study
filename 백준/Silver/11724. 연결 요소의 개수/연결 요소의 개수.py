import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True  # BFS 호출 전에 방문 처리

    while queue:
        node = queue.popleft()
        for neighbor in connected[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 빠른 입력 사용
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
connected = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

# 간선 정보 추가
for _ in range(M):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

# 연결 요소 개수 계산
result = 0
for i in range(1, N + 1):
    if not visited[i]:  # 방문하지 않은 노드라면 BFS 실행
        bfs(i)
        result += 1

print(result)