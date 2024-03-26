import sys
si = sys.stdin.readline 

N = int(si())
acbo_list = list(map(int, si().split()))
Q = int(si())
question_list = []

for i in range(Q):
    question_list.append(list(map(int, si().split())))


prefix_sum_list = [0 for i in range(N + 1)]

for i in range(N - 1):
    if acbo_list[i] > acbo_list[i+1]:
        prefix_sum_list[i+1] = prefix_sum_list[i] + 1
    else:
        prefix_sum_list[i+1] = prefix_sum_list[i]

prefix_sum_list[N] = prefix_sum_list[N - 1]

for x, y in question_list:
    print(prefix_sum_list[y - 1] - prefix_sum_list[x - 1]) 