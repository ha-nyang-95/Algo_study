'''
위상정렬
그래프, 즉 자식노드만 만들어주고
자식을 지칭하는 idx에 맞는 parent의 수를 +1 해준다.

parent에 부모가 0인 idx를 heap에 저장 후 시작
heap에서 꺼내며 출력해줄 result에 추가
이후, idx에 해당하는 자식 노드들의 parent수를 -1 해주며,
부모 수가 0이 되면 heap에 추가한다.
'''

import heapq

for tc in range(1,11):
    V,E=map(int,input().split())
    graph=list(map(int,input().split()))
    child = [[] for _ in range(V+1)]
    parent = [0 for _ in range(V+1)]

    # 해당하는 idx의 부모의 수와 자식 리스트를 작성
    for i in range(0,len(graph),2):
        a,b=graph[i],graph[i+1]
        parent[b]+=1
        child[a].append(b)

    # 시작할 노드를 구한다.
    heap=[]
    for j in range(1,V+1):
        if not parent[j]:
            heapq.heappush(heap, j)

    # 반복문을 돌며, 작업 순서를 정한다.
    result=[]
    while heap:
        idx = heapq.heappop(heap)
        result.append(idx)
        
        # idx가 부모라면, 부모 중 하나는 이미 지나간 것이니
        # parent에 해당하는 인덱스에 -1을 해준다.
        # 이후, 자신의 인덱스에 해당하는 parent의 수가 0이 되면
        # heap에 추가한다.
        for node in child[idx]:
            parent[node]-=1
            if not parent[node]:
                heapq.heappush(heap, node)

    print(f'#{tc} {" ".join(map(str, result))}')