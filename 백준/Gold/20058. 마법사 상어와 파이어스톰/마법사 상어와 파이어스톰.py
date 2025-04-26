'''
2**N * 2**N 의 격자판
파이어스톰을 시전하기 전 2**L * 2**L로 나눈
격자판을 90도 회전시킨다.
이후, 상하좌우로 3칸 이상 얼음이 차있지 않다면,
얼음 칸의 개수를 -1 해준다.

남아 있는 얼음 칸의 합과 개수를 구하라.
그렇다면, 회전을 시킨 뒤,
얼음 칸의 개수를 빼주는 단계에서 기준이 되는 칸을
모두 더하는 변수와 0이 아니라면 개수를 세주는 변수를
생성하면 추가로 반복문을 작성하지 않아도 될듯
'''
import copy
# import sys
# sys.stdin = open('testcases/1/input.txt')
from collections import defaultdict

N,Q = map(int,input().split())
ice_block = [list(map(int,input().split())) for _ in range(2**N)]
L = list(map(int,input().split()))

t=0
while t<Q:
    test_block = [[0 for _ in range(2**N)] for _ in range(2**N)]
    change=defaultdict(list)
    for i in range(2**L[t]):
        for j in range(2**L[t]):
            change[(i,j)].append((j,2**L[t]-1-i))

    # 1. 2**L의 맞게 격자판을 회전시켜야 한다.
    for r in range(0,2**N,2**L[t]):
        for c in range(0,2**N,2**L[t]):
            for a in range(r,r+2**L[t]):
                for b in range(c,c+2**L[t]):
                    cur_a,cur_b=a-r,b-c
                    test_a,test_b = change[(cur_a,cur_b)][0]
                    change_a,change_b=test_a+r,test_b+c
                    test_block[change_a][change_b]=ice_block[a][b]

    # 2. 각 얼음판의 주변에 3개 이상의 얼음칸이 있는지 확인
    break_ice=[]
    for r in range(2**N):
        for c in range(2**N):
            count=0
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc=r+dr,c+dc
                if not (0<=nr<2**N and 0<=nc<2**N) or not test_block[nr][nc]:
                    continue
                count+=1
            if count<3:
                break_ice.append((r,c))

    for r,c in break_ice:
        if test_block[r][c]>0:
            test_block[r][c]-=1

    ice_block=copy.deepcopy(test_block)
    t+=1

# 3. 남아있는 얼음의 개수와 가장 큰 덩어리를 구함
ice_total=sum(map(sum,ice_block))
ice_count=0
for r in range(2**N):
    for c in range(2**N):
        if not ice_block[r][c]:
            continue
        stack=[(r,c)]
        ice_block[r][c]=0
        count=0
        while stack:
            r,c=stack.pop()
            count+=1
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc=r+dr,c+dc
                if not (0<=nr<2**N and 0<=nc<2**N) or not ice_block[nr][nc]:
                    continue
                stack.append((nr,nc))
                ice_block[nr][nc]=0

        ice_count=max(ice_count,count)

print(ice_total)
print(ice_count)