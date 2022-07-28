# 2022-05-15
# 2022-07-28
# 소수의 연속합
import sys
si = sys.stdin.readline

N = int(si())
# 1. 소수 배열 만들기 - 에라토스의 체
# 0, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12 
prime_num = [False, False] + [True] * (N-1)
prime_list = []
for i in range(2, len(prime_num)):
    if prime_num[i] == True:
        prime_list.append(i)
        for j in range(i*i, len(prime_num), i):
            prime_num[j] = False # 소수가 안되므로

# 2. 연속된 소수의 합으로 표현가능한지 체크
# 투포인터
interval_sum = 0
end = 0
answer = 0
start = 0
while True:
    if interval_sum >= N:
        if interval_sum == N:
            answer += 1
        interval_sum = interval_sum - prime_list[start]
        start += 1
    elif end == len(prime_list):
        break
    else:
        interval_sum += prime_list[end]
        end += 1
print(answer)