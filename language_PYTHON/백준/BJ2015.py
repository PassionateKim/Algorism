import sys
si = sys.stdin.readline 
N, K = map(int, si().split())

arr = list(map(int, si().split()))

prefix_sum = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]


my_dict = dict()
answer = 0
for i in range(N + 1):
    answer = answer + my_dict.get(prefix_sum[i] - K, 0)

    my_dict[prefix_sum[i]] = my_dict.get(prefix_sum[i], 0) + 1

print(answer)