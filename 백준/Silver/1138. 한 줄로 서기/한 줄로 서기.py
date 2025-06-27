'''
줄을 선 순서대로 키를 출력한다.

첫번째 줄에는 몇명인지
두번째 줄에는 키가 1인 사람부터
자신의 왼쪽에 자신보다 키가 큰 사람이
몇 명있었는지 작성한다.

고로, 키가 1인 사람부터 말하기 때문에,
왼쪽으로 몇 칸을 비우고 서있었는지 판단 가능한 수치
'''
# import sys
# sys.stdin = open('testcases/1/input.txt')

N = int(input())
h = list(map(int,input().split()))
# print(h)
result =[0 for _ in range(N)]
# print(result.index(0))

# h를 순서대로 읽으며, h의 index가 왼쪽으로부터
# 몇 칸 이동하여 입력되어야 하는지 판단 후, result에 입력
# i는 h에서 몇번째의 키의 사람인지 판단하는 지표
for i in range(N):
    # cnt는 h의 value만큼 왼쪽으로 0의 개수를 세줄 지표
    cnt=0
    # j는 result내의 위치를 판단
    for j in range(N):
        if not h[i]:
            break
        if cnt == h[i]:
            if not result[j]:
                result[j]=i+1
                break
            else:
                continue
        if not result[j]:
            cnt+=1
    if not cnt:
        for t in range(N):
            if not result[t]:
                result[t] = i+1
                break
    # print(*result)

print(*result)

