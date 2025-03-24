from collections import defaultdict

# 단어의 개수
N = int(input())
alp = list(input().strip() for _ in range(N))
# 단어의 가중치를 나타낼 딕셔너리
# 단어의 알파벳의 위치를 통해 숫자의 각 자리수를 알파벳의 value값에
# 모두 더해준다.
# 예를 들어) 'ABC' => 'A':100, 'B':10, 'C'=1
dic = defaultdict(int)

for word in alp:
    for i in range(len(word)):
        dic[word[i]] += 10 ** (len(word) - 1 - i)

# dic.items()가 ('A',10000),('B',1010)
# 이런 식으로 저장되어 있으면, 뒤의 수를 기준으로
# 내림차순으로 정리한다.
alp_weight = sorted(dic.items(), key=lambda x: -x[1])

# 가중치가 제일 높은 알파벳 순서대로
# 가장 높은 수인 9부터 곱해줘
# 모두 더한다.
num = 9
result = 0
for a, v in alp_weight:
    result += v * num
    num -= 1

print(result)