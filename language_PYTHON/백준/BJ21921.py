# 블로그
# 복습 횟수:1, 00:30:00, 복습필요O
import sys
si = sys.stdin.readline 

N, X = map(int, si().split())
answer = 0
arr = list(map(int, si().split()))
sum_list = list()
if max(arr) == 0:
    print("SAD")
else:
    candidate_sum = sum(arr[0:X])

    sum_list.append(candidate_sum)

    answer = max(answer, candidate_sum)

    minus_index = 0
    plus_index = X
    while plus_index != len(arr):
        candidate_sum = candidate_sum - arr[minus_index]
        candidate_sum = candidate_sum + arr[plus_index]

        answer = max(answer, candidate_sum)
        sum_list.append(candidate_sum)

        minus_index += 1
        plus_index += 1


    print(answer)
    print(sum_list.count(answer))
