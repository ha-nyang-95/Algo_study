from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    home_x,home_y = map(int,input().split())
    stores = []
    for _ in range(n):
        x,y = map(int,input().split())
        stores.append((x,y))
    festival_x,festival_y = map(int,input().split())

    q=deque()
    q.append((home_x,home_y))
    # 편의점을 방문했는지 안했는지 체크하기 위한 배열
    visited = [False for _ in range(n)]
    # 맥주를 마시며 파티장에 도달할 수 있는지 확인
    while q:
        r,c = q.popleft()
        # 현재 위치에서 페스티벌장까지 도달할 수 있는지 체크
        # 1000보다 작거나 같은 이유는
        # 현 위치는 집이거나 편의점일 거기 때문에
        # 맥주는 항상 20병이라 20*50이 갈 수 있는 거리가 된다.
        if abs(r-festival_x)+abs(c-festival_y)<=1000:
            print('happy')
            break

        # 현 위치에서 페스티벌장을 갈 수 없기 때문에,
        # 편의점을 들려야 한다.
        # 편의점 개수만큼 반복문을 돌며
        # 편의점을 방문한 적이 있는지 체크 후,
        # 현 위치에서 편의점이 방문 가능한지 체크한다.
        for i in range(n):
            if not visited[i]:
                x,y=stores[i]
                if abs(r-x)+abs(c-y)<=1000:
                    visited[i]=True
                    q.append((x,y))
    else:
        print('sad')