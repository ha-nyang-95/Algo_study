from itertools import combinations
from collections import deque

girls = [list(input()) for _ in range(5)]
girls_array = [(i, j) for i in range(5) for j in range(5)]
result = 0

for comb in combinations(girls_array, 7):
    comb_list = [girls[x][y] for x, y in comb]
    if comb_list.count('Y') > 3:
        continue
    visited = set()
    q = deque([comb[0]])
    visited.add(comb[0])

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < 5 and 0 <= nc < 5):
                continue
            if (nr, nc) not in comb or (nr, nc) in visited:
                continue
            q.append((nr, nc))
            visited.add((nr, nc))
    if len(visited) == 7:
        result += 1

print(result)