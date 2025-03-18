# 코드 해석
# 1. 입력 처리
#     •	N(직원 수)을 입력받고, 직속 상사 정보 리스트(parents)를 입력받습니다.
# 2. 트리 구성
#     •	children[i]에 i번 직원의 직속 부하 직원들을 저장하기 위한 2차원 리스트를 만듭니다.
#     •	-1인 인덱스가 **사장(루트)**이므로, 이를 root 변수에 저장합니다.
#     •	그 외의 경우, parents[i]가 p라면, “p번 직원의 자식이 i”임을 의미하므로
#       children[p].append(i)를 합니다.
# 3. 재귀 함수 get_time(employee)
#     •	입력: 특정 직원 번호
#     •	출력: 해당 직원이 자신의 모든 부하(서브트리 전체)에게 소식을 전하는 데 걸리는 시간
#     •	처리:
#     1. 부하가 없는 경우(leaf 노드)는 0을 반환 (전화할 대상이 없음).
#     2. 각 부하별로 재귀 호출을 하여, 부하가 자신의 서브트리에 소식을 전하는 데 걸리는 시간을 구합니다.
#     3. 가장 오래 걸리는 부하부터 전화를 걸어야 전체 시간을 최소화할 수 있으므로,
#        서브트리 시간을 내림차순 정렬합니다.
#     4. i번째로 전화할 때는 i+1분 후에 부하가 전화를 받기 시작하고, 그 부하의 서브트리 시간이 t라면,
#     \text{finish_time} = (i+1) + t 가 됩니다.
#     5. 그 중 최대값이 해당 직원의 전체 소식 전달 완료 시간이 됩니다.
# 4. 결과 출력
#     •	root(사장)에게 get_time을 호출한 결과를 출력합니다.

def solve():
    N = int(input().strip())
    parents = list(map(int, input().split()))
    # [-1, 0, 0, 2, 2]

    # 1. 트리 구성 (인접 리스트)
    #    children[i] = i번 직원의 직속 부하 직원 리스트
    children = [[] for _ in range(N)]
    # [[1, 2], [], [3, 4], [], []]
    root = 0  # 사장(루트) 직원 번호를 저장할 변수

    for i in range(N):
        p = parents[i]
        if p == -1:
            root = i  # 사장(루트) 노드
        else:
            children[p].append(i)

    # 2. 각 노드(직원)별로 "자신의 부하 전체에게 소식 전달 완료 시간"을 구하는 재귀 함수
    def get_time(employee):
        # 자식(부하)이 없으면 더 이상 전화할 대상이 없으므로 0분
        if not children[employee]:
            return 0

        # 각 자식의 "소식 전달 완료 시간"을 재귀적으로 구함
        times = []
        for child in children[employee]:
            times.append(get_time(child))
        # 서브트리 시간이 긴 순서대로 내림차순 정렬
        times.sort(reverse=True)
        # 자식에게 전화를 걸 때 i번째로 전화한다면,
        # "i+1분 후에 자식이 전화를 받기 시작" + "자식의 서브트리 완료 시간"
        # 최종적으로 가장 늦게 끝나는 시간이 이 노드의 소식 전달 완료 시간
        max_finish = 0
        for i, t in enumerate(times):
            finish_time = (i + 1) + t
            if finish_time > max_finish:
                max_finish = finish_time

        return max_finish

    # 3. 사장(루트)의 "소식 전달 완료 시간"이 최종 답
    answer = get_time(root)
    print(answer)

solve()