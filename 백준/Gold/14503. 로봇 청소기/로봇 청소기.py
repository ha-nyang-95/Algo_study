from collections import deque, defaultdict

# 북(0) 동(1) 남(2) 서(3)
dic = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
clean = [list(map(int, input().split())) for _ in range(N)]

queue = deque([(r, c, d)])
clean[r][c] = 2
while queue:
    r, c, d = queue.popleft()
    for _ in range(4):
        d -= 1
        if d < 0:
            d += 4
        nr, nc = r + dic[d][0], c + dic[d][1]
        if 0 <= nr < N and 0 <= nc < M and clean[nr][nc] == 0:
            queue.append((nr, nc, d))
            clean[nr][nc] = 2
            break
    else:
        nr, nc = r + dic[d - 2][0], c + dic[d - 2][1]
        if 0 <= nr < N and 0 <= nc < M:
            if clean[nr][nc] == 1:
                break
            else:
                queue.append((nr, nc, d))

result = 0
for line in clean:
    result += line.count(2)
print(result)