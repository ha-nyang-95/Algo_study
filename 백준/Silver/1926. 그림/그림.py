'''
그림의 개수와 그림들 중 최대 면적을 구하는 문제
먼저, 각 위치를 돌며 1을 찾고 1을 찾으면 연결된 곳이 끝날때까지
반복하며 면적을 구한다.
연결된 곳이 끝난다면, 그때 그림의 개수를 세준다.
'''
from collections import deque
# import sys
#
# sys.stdin = open('testcases/1/input.txt')

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
# print(paper)
# 그림의 개수와 최대 면적을 구해줄 변수
paint_count = 0
paint_max = 0

# 각 좌표를 돌며 1을 찾아 그림의 위치를 찾는다.
for i in range(n):
    for j in range(m):
        # 그림의 시작점을 찾았다면 반복문을 통해 그림의 면적을 구한다.
        if paper[i][j] == 1:
            # 찾은 지점은 0으로 만들어줘 반복탐색을 방지한다.
            q = deque([(i, j)])
            paper[i][j] = 0
            paint = 1
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                        q.append((nx, ny))
                        paper[nx][ny] = 0
                        paint += 1
            # 반복문이 종료되었다면 하나의 그림의 면적을 구하는 것이
            # 종료되었다는 의미이니 그림의 개수와 최대 면적값을 갱신
            paint_count += 1
            paint_max = max(paint_max, paint)

print(paint_count)
print(paint_max)
