import sys
si = sys.stdin.readline 

# 학생 수, 졸고 있는 학생 수, 출석 코드 보낼 학생 수, 주어질 구간의 수 
N, K, Q, M = map(int, si().split())
s = list(map(int, si().split()))
code_list = list(map(int, si().split()))

sleeping_set = set(s)

interval_list = []

for i in range(M):
    front, back = map(int, si().split())
    interval_list.append([front, back])

have_list = [0 for i in range(N+2 + 1)]

# 1. 구간 별 누적합 세팅
for code in code_list:
    if code in sleeping_set:
        continue

    mul = 0
    while True:
        mul += 1
        val = code * mul
        
        if val > N+2:
            break

        if val in sleeping_set:
            continue

        have_list[val] = 1 # 출석 코드를 전달

# 누적합 구하기
prefix_sum_list = [0 for i in range(N+2 + 1)]

for index in range(1, len(have_list)):
    prefix_sum_list[index] = have_list[index] + prefix_sum_list[index - 1]

for front, back in interval_list:
    present_num = prefix_sum_list[back] - prefix_sum_list[front - 1]

    print((back - front + 1) - present_num)