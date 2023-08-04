# 숫자 카드
# 복습 횟수:2, 00:10:00, 복습필요X
import sys
si = sys.stdin.readline 

N = int(si())
own_list = list(map(int, si().split()))
own_list.sort()

M = int(si())
check_card_list = list(map(int , si().split()))

own_dict = dict()

for own in own_list:
    if own not in own_dict.keys():
        own_dict[own] = 1


for check_card in check_card_list:
    if check_card in own_dict.keys():
        print(1, end = " ")
    else:
        print(0, end = " ")