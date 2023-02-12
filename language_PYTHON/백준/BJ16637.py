# 괄호 추가하기
# 복습 횟수:0, 02:00:00, 복습필요O
import sys
from itertools import combinations
si = sys.stdin.readline
N = int(si())
oper_list = list(map(str, si().rstrip()))

answer = -2**31
oper_num = N//2

def first_cal(f_l):
    arr = []
    i = 0

    while i < len(oper_list):
        if i in f_l:
            a = arr.pop()
            if oper_list[i] == '+':
                num = int(a) + int(oper_list[i+1])
                arr.append(str(num))
                i += 2
            elif oper_list[i] == '-':
                num = int(a) - int(oper_list[i+1])
                arr.append(str(num))
                i += 2
            else:
                num = int(a) * int(oper_list[i+1])
                arr.append(str(num))
                i += 2
        else:
            arr.append(oper_list[i])
            i += 1

    return arr

def last_cal(f_li):
    number = int(f_li[0])

    for i in range(1, len(f_li) -1, 2):
        if f_li[i] == '+':
            number += int(f_li[i+1])
        elif f_li[i] == '-':
            number -= int(f_li[i+1])
        else:
            number *= int(f_li[i+1])
            
    return number

for count in range((oper_num+1)//2 + 1): # count 가능한 괄호의 개수
    oper_idx = [i for i in range(1, N, 2)]
    candidate_opers = list(combinations(oper_idx, count))
    real_opers_idx = []
    # 차이가 2인것이 하나라도 있는 경우는 빼기
    for candidate in candidate_opers:
        flag = 1
        for i in range(len(candidate)-1):
            if candidate[i+1] == candidate[i] + 2: 
                flag = 0
                break
        if flag:
            real_opers_idx.append(candidate)
    
    # 괄호있는 값을 계산 한 것을 치환해야함 - 첫번째 계산
    if len(real_opers_idx[0]) != 0: 
        for real_opers in real_opers_idx: #[(1, 5) (1, 7)]
            first_list = first_cal(real_opers)
            # 순서대로 계산하기
            
            result = last_cal(first_list)
            answer = max(answer, result)
    else: # 괄호가 없는 경우 
        result = last_cal(oper_list)
        answer = max(answer, result)

print(answer)       