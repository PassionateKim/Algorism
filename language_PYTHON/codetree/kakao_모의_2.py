import sys
from collections import defaultdict
si = sys.stdin.readline 

N, K = map(int, si().split())

candidate_list = list(map(int, si().split()))

candidate_dict = defaultdict(int)


for candidate in candidate_list:
    candidate_dict[candidate] += 1


sorted_dict = sorted(candidate_dict.items(), reverse=True)

answer = -1

for key, value in sorted_dict:
    if value >= K:
        answer = key
        break

print(answer)