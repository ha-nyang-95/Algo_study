for tc in range(1, int(input()) + 1):
    N = int(input())
    rank_old = list(map(int, input().split()))
    M = int(input())
    rank_new = [[] for _ in range(N)]
    for i in range(N):
        rank_new[i].append(rank_old[i])
    for _ in range(M):
        a, b = map(int, input().split())
        a_index, b_index = rank_old.index(a), rank_old.index(b)
        for i in range(N):
            if a in rank_new[i]:
                a_new_index = i
                rank_new[a_new_index].remove(a)
            if b in rank_new[i]:
                b_new_index = i
                rank_new[b_new_index].remove(b)
        if a_index > b_index:
            a_new_index -= 1
            b_new_index += 1
            rank_new[a_new_index].append(a)
            rank_new[b_new_index].append(b)
        else:
            a_new_index += 1
            b_new_index -= 1
            rank_new[a_new_index].append(a)
            rank_new[b_new_index].append(b)

    for line in rank_new:
        if not line:
            print('IMPOSSIBLE')
            break
    else:
        for line in rank_new:
            print(*line, end=' ')
        print()