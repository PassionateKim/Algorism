from collections import defaultdict
import sys
si = sys.stdin.readline 
N, M = map(int, si().split())
candidate_list = list(map(int, si().split()))

my_dict = defaultdict(int)

for candidate_int in candidate_list:
    my_dict[candidate_int] += 1


candidate_value_list = []
    
for value, count in my_dict.items():
    if count >= M:
        candidate_value_list.append(value)
        

candidate_value_list.sort(reverse=True)
if len(candidate_value_list) == 0:
    print(-1)
else:
    print(candidate_value_list[0])