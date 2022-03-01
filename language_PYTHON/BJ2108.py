#통계학 
from collections import Counter
import sys


#1.-4000~4000 이니까 개수 8001개 
value_list  = []
N = int(input())
for _ in range(N):
    value_list.append(int(sys.stdin.readline()))

value_list.sort()

print((round(sum(value_list)/N)))
print(value_list[len(value_list)//2])

mode_dict = Counter(value_list)

modes = mode_dict.most_common()
print(modes)
print(len(modes))
# if len(value_list) > 1:
#     if(modes[0][1]== modes[1][1]):
#         print(modes[1][0])
#     else:
#         print(modes[0][0])
# else:
#     print(modes[0][0])
# print(max(value_list)-min(value_list))