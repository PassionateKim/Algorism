
from math import gcd
# 가로수
N = int(input())
garosu_list = [int(input()) for _ in range(N)]
differ_list = []
for i in range(len(garosu_list)-1):
    differ_list.append(abs(garosu_list[i]-garosu_list[i+1]))



value = gcd(*differ_list)
answer = 0

for item in differ_list:
    tmp = (item // value) - 1
    answer += tmp

print(answer) 

