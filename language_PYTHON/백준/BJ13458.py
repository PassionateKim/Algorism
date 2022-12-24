# 시험 감독
import sys
import math
si = sys.stdin.readline

N = int(si())
people_list = list(map(int, si().split()))
main_, sub_ = map(int, si().split())
answer = N
for people in people_list:
    people = people - main_

    if (people < 0):
        continue 
    
    tmp = math.ceil((people / sub_))
    answer = answer + tmp

print(answer)