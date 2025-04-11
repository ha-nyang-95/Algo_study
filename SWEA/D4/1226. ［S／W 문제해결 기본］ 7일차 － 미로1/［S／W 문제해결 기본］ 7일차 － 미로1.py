from collections import deque

T = 10
for _ in range(T):
    N = int(input())
    mirro = [list(map(int, input())) for _ in range(16)]
    
    # 모든 경우의 출발점은 (1,1)
    q = deque([(1, 1)])
    # 반복문을 돌며 (13,13) 위치에 도달하는지 체크
    # => 도달한다면, 1을 출력 후 반복문 종료
    # 0이 있다면 2로 바꿔주고 위치를 저장하며 계속 진행
    # => 반복문이 종료될 때까지 (13,13)에 도달하지 못했다면,
    #    0을 출력
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nr == 13 and nc == 13:
                print(f'#{N} 1')
                break
            if 0 <= nr < 16 and 0 <= nc < 16 and not mirro[nr][nc]:
                mirro[nr][nc] = 2
                q.append((nr, nc))
        else:
            continue
        break
    else:
        print(f'#{N} 0')