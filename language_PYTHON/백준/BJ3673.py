import sys
si = sys.stdin.readline 
C = int(si())

for i in range(C):
    D, N = map(int, si().split())
    arr = list(map(int, si().split()))

    prefix_sum = [0 for i in range(N + 1)]

    # 누적합
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
    
    sub_dict = dict()
    answer = 0

    for index, val in enumerate(prefix_sum):
        answer = answer + sub_dict.get(val % D, 0)
        sub_dict[val % D] = sub_dict.get(val % D, 0) + 1
    
    print(answer)