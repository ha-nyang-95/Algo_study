def backtracking(cur, cost):
    global result
    if result <= cost:
        return
    if sum(visited_city) == N - 1:
        if move_cost[cur][0]:
            result = min(result, cost + move_cost[cur][0])
            return
        else:
            return

    for i in range(1, N):
        if move_cost[cur][i] and not visited_city[i]:
            visited_city[i] = True
            backtracking(i, cost + move_cost[cur][i])
            visited_city[i] = False

N = int(input())
move_cost = [list(map(int, input().split())) for _ in range(N)]
visited_city = [False for _ in range(N)]
result = float('inf')
backtracking(0, 0)
print(result)