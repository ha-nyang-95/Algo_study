'''
단순히 높이로 판단하는 것이 아닌,
기울기로 보아 고층 건물에서 상대적으로 낮은 건물과의
시야를 가로막는 건물이 있는지 판별해야 한다.
즉, 기울기의 크기로 판별
고층 건물 기준으로
오른쪽은 기울기가 상승해야 보이고,
왼쪽은 기울기가 하강해야 보인다.
'''

N = int(input())
building = list(map(int,input().split()))

# 기준이 되는 건물과 비교를 해야한다.
# 매 기준이 되는 건물마다 각 건물과 기울기 비교를 해야한다.
# 이때, 기준이 되는 건물의 순서보다 작다면 왼쪽, 그렇지 않다면 오른쪽
idx = 0
max_count = 0

while idx<N:
    # 건물이 한개보다 이하이면 보이는 건물을 세어줄 필요없다.
    if N<=1:
        print(0)
        break
    # 건물 기준으로 각 건물의 기울기 비교를 해야한다.
    # 기준 건물과 가까운 건물부터 기울기를 계산해가며 건물을 세어야하기 때문에
    # 왼쪽과 오른쪽의 반복문을 각자 수행해야 한다.
    # 이때, X=i, Y=building[i]
    count=0
    # 주의해야 할점은 변수들의 들어갈 값들이 음수부터 양수까지
    # 다양하게 비교해야 하기 때문에
    # 습관적으로 max 값을 0으로 설정하는 것을 주의해야 한다.
    min_inc=float('inf')
    max_inc=float('-inf')
    # 왼쪽
    for i in range(idx-1,-1,-1):
        inc = (building[idx]-building[i])/(idx-i)
        if inc<min_inc:
            count+=1
            min_inc=inc
    # 오른쪽
    for j in range(idx+1,N):
        inc = (building[idx]-building[j])/(idx-j)
        if inc>max_inc:
            count+=1
            max_inc=inc

    max_count = max(max_count,count)
    idx+=1
else:
    print(max_count)