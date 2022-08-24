# 2022-05-15
# 2022-07-28
# 2022-07-29
# 2022-08-24
# 소수의 연속합
import sys
si = sys.stdin.readline

n = int(si())

# 1. 소수 구하기
prime_list = []
prime_check = [False, False] + [True] * (n-1)
for i in range(2, n+1):
    if prime_check[i]:
        prime_list.append(i)
        for j in range(i*i, n+1, i):
            prime_check[j] = False

# 2. 연속합 -> 투 포인터
left = 0
right = 0
answer = 0
interval_sum = 0
while True:
    if interval_sum >= n:
        if interval_sum == n:
            answer += 1
        # left 한칸 당기기
        interval_sum -= prime_list[left]
        left += 1
    elif right == len(prime_list):
         break
    else:
        interval_sum += prime_list[right]
        right += 1
    
print(answer)