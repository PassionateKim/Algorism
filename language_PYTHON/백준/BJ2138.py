# 전구와 스위치
# 복습 횟수:0, 00:45:00, 복습필요O
import sys
from copy import deepcopy
si = sys.stdin.readline
N = int(si())

current_state = list(map(int, si().rstrip()))
wanted_state = list(map(int, si().rstrip()))

def check():
    answer = 0
    tmp = deepcopy(current_state) 
    # 첫번째 전구를 키지 않는 경우
    for i in range(1, len(tmp)):
        if tmp[i-1] != wanted_state[i-1]:
            if tmp[i-1] == 0:
                tmp[i-1] = 1
            else:
                tmp[i-1] = 0
            
            if tmp[i] == 0:
                tmp[i] = 1
            else:
                tmp[i] = 0

            if i != len(tmp) - 1:
                if tmp[i+1] == 0:
                   tmp[i+1] = 1
                else:
                    tmp[i+1] = 0
            
            answer += 1

    if tmp == wanted_state:
        return answer

    # 첫번째 전구를 키는 경우
    answer = 1

    tmp = deepcopy(current_state)

    if tmp[0] == 0:
        tmp[0] = 1
    else:
        tmp[0] = 0
    
    if tmp[1] == 0:
        tmp[1] = 1
    else:
        tmp[1] = 0

    for i in range(1, len(tmp)):
        if tmp[i-1] != wanted_state[i-1]:
            if tmp[i-1] == 0:
                tmp[i-1] = 1
            else:
                tmp[i-1] = 0
            
            if tmp[i] == 0:
                tmp[i] = 1
            else:
                tmp[i] = 0

            if i != len(tmp) - 1:
                if tmp[i+1] == 0:
                   tmp[i+1] = 1
                else:
                    tmp[i+1] = 0
            
            answer += 1

    if tmp == wanted_state:
        return answer
    
    return -1

print(check())