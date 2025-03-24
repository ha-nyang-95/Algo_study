from collections import deque

# 전체 사람의 수
n = int(input())
# 서로 다른 두 사람의 번호
a, b = map(int, input().split())

# 관계의 개수
m = int(input())
# 관계들을 저장할 리스트
relations = [None] + [[] for _ in range(n)]
# 관계들을 양방향으로 저장
for _ in range(m):
    c, d = map(int, input().split())
    relations[c].append(d)
    relations[d].append(c)

# 양방향으로 이동하며 방문 체크할 리스트
visited = [False for _ in range(n + 1)]
# 최종값을 마지막에 저장
result = 0

# 큐에 두 사람의 번호 중 하나(a)와 촌수를 세줄 숫자를 넣어준다.
queue = deque([(a, 0)])
visited[a] = True
while queue:
    t, c = queue.popleft()
    # 각 위치에 양방향으로 관계있는 사람들을 체크
    for i in relations[t]:
        # 두 사람 중 나머지(b)를 찾으면 반복문을 탈출
        if i == b:
            result = c + 1
            break
        # 방문하지 않은 곳들을 추가하며
        # 촌수를 하나씩 올려준다.
        if not visited[i]:
            queue.append((i, c + 1))
            visited[i] = True
    else:
        continue
    break

# result의 값이 변하지 않았다면,
# 촌수로 이어져 있는 게 아니기 때문에
# -1을 출력
# 변했다면 result를 출력
if not result:
    print(-1)
else:
    print(result)
