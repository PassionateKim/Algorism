import sys
si = sys.stdin.readline 
N, L = map(int, si().split())
arr = list(map(int, si().split()))

interval_list = [[-1, -1]]
for val in arr:
    interval_list.append([val - L, val + L])


prefix_sum_list = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    prefix_sum_list[i] = prefix_sum_list[i - 1] + arr[i - 1]

isStable = True

for i in range(1, N):
    left, right = interval_list[i]

    total = prefix_sum_list[N] - prefix_sum_list[i]
    divider = N - i

    check = total / divider

    if not (left < check < right):
        isStable = False
        break

if isStable:
    print("stable")
else:
    print("unstable")