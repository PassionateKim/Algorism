import sys
si = sys.stdin.readline 

N = int(si())
arr = list(map(int, si().split()))

prefix_sum = []
prefix_sum.append(arr[0])
# prefix_sum = [x1, x1 + x2, x1 + x2 + x3, x1 + x2 + x3 + x4 ... ]
for i in range(1, N):
    prefix_sum.append(arr[i] + prefix_sum[i-1])

answer = 0

for index, value in enumerate(prefix_sum):
    answer = answer + arr[index] * (prefix_sum[N - 1] - prefix_sum[index])

print(answer)