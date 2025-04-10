def recur(cur):
    global count, remove_point
    # 자식 노드가 없다면 카운트를 하나 세준다.
    if not tree[cur]:
        count += 1
        return
    
    # 자식 노드에 제거할 노드가 있다면,
    # 제거 노드는 재귀를 돌지 않는다.
    # 이때, 자식 노드가 하나인 노드라면,
    # 제거 노드가 사라지면 자식이 없는 노드가 되기 때문에
    # 카운트를 하나 세준다.
    for j in tree[cur]:
        if j == remove_point:
            if len(tree[cur]) == 1:
                count += 1
            continue
        recur(j)

N = int(input())
# 자식 노드를 저장할 부모 노드 리스트
# [[1, 2], [3, 4], [], [], []]
tree = [[] for _ in range(N)]
child = list(map(int, input().split()))
# 시작 노드가 0이 아닌 경우도 있기 때문에,
# -1이 나오면 start_point로 저장을 해준다.
for i in range(0, N):
    if child[i] == -1:
        start_point = i
        continue
    tree[child[i]].append(i)

# 제거할 노드와 시작할 노드가 같다면 0을 출력하고,
# 그게 아니라면 시작 노드부터 재귀함수를 돌려 자식 노드가 없는
# 노드들의 개수를 세준다.
remove_point = int(input())
if remove_point == start_point:
    print(0)
else:
    count = 0
    recur(start_point)
    print(count)