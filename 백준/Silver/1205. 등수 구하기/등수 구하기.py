'''
랭킹 리스트(P)에 몇 등인지 출력하는 문제
랭킹 리스트에 들 수 없는 등수라면 -1 을 출력
즉, 기존에 있는 리스트(N)와 태수의 점수를 비교해,
태수의 점수가 몇등인지 판별하고, 태수의 점수가 리스트안에
속할 수 있는지 판별 후 속한다면 몇 등인지 출력,
속하지 못한다면 -1을 출력한다.
'''

N, s, P = map(int,input().split())
if N>0:
    score = list(map(int,input().split()))

    # s가 score와 비교했을때 작거나 같으면 등수를 하나씩 올린뒤,
    # 최종 등수가 10보다 크다면 바로 -1 출력
    # 최종 등수가 10보다 작거나 크다면 같은 수가 있는지
    # 앞에서부터 검사하여 있다면, 그 등수로 최종 마무리 한다.
    a=1
    b=0
    for i in range(N):
        if score[i]>=s:
            a+=1
            if not b and score[i]==s:
                b=i+1
        else:
            break

    if a>P:
        print(-1)
    else:
        if b:
            print(b)
        else:
           print(a)

else:
    print(1)