'''
a와 b가 섞여있는 문자열 중 a가 연속적인 문자열이 만들어질 수 있는 경우는
a의 개수만큼 첫번째 위치부터 괄호로 묶어 이를 끝 위치까지 반복한 수다.
이때, 각 경우마다 괄호안에 b가 몇개있는지 확인하고,
b의 개수가 가장 작은 값을 출력한다.
'''

alp = input()
n = len(alp)
a_count = alp.count('a')
alp += alp[0:a_count]
min_result = float('inf')

for i in range(n):
    min_result = min(min_result, alp[i:i+a_count].count('b'))

print(min_result)