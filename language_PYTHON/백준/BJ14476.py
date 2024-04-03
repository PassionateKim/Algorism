import math
import sys
si = sys.stdin.readline 
N = int(si())
arr = list(map(int, si().split()))

answer = -1
answer2 = -1
# def gcd(x, y):
#     while y:
#         x, y = y, x % y

#     return x

left_prefix_list = [arr[0]]
right_prefix_list = [arr[-1]]


# left prefix
left = left_prefix_list[0]
for i in range(1, N):
    left = math.gcd(left, arr[i])
    left_prefix_list.append(left)

# right prefix
right = right_prefix_list[0]
for i in range(N-2, -1, -1):
    right = math.gcd(right, arr[i])    
    right_prefix_list.append(right)

right_prefix_list.reverse()

for index in range(N):
    if index == 0:
        val = right_prefix_list[index + 1]
        # 이때, 최대공약수는 K의 약수가 되면 안 된다.
        
    if 0 < index < N - 1:
        left_val = left_prefix_list[index - 1]
        right_val = right_prefix_list[index + 1]
        val = math.gcd(left_val, right_val)

    if index == N-1:
        val = left_prefix_list[index - 1]
    
    if (arr[index] % val == 0) : continue 

    if answer < val:
        answer = val
        answer2 = arr[index]

if answer == -1:
    print(-1)
else:
    print(answer, answer2)