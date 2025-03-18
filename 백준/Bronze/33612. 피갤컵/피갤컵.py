N = int(input())
pigalcup = [2024, 8]

for _ in range(1, N):
    pigalcup[1] += 7
    if pigalcup[1] > 12:
        pigalcup[0] += 1
        pigalcup[1] -= 12

print(*pigalcup)
