# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import defaultdict
si = sys.stdin.readline

N, M = map(int, si().split())
num_list = list(map(int, si().split()))
mydict = defaultdict(int)

for num in num_list:
    if(num not in mydict.keys()):
        mydict[num] = 1 
    else:
        mydict[num] += 1

sorted_dict = sorted(mydict.items(), key = lambda x: [x[1], x[0]], reverse=True)
candidate_dict = sorted_dict[:M]
for i in range(M):
    print(candidate_dict[i][0], end=' ')