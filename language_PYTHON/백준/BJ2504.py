# 괄호의 값
import sys
si = sys.stdin.readline

# 올바른 괄호열인지 체크하는 함수
def isOk(arr):
    soe = [] # 소괄호
    dae = [] # 대괄호
    flag = -1 # 초기상태

    for i in range(len(arr)):
        # 소괄호
        if arr[i] == '(' or arr[i] ==')':
            if arr[i] == '(':
                soe.append('(')
                flag = 0
            else: # == ')'
                if soe and (flag == 0 or flag == -1):
                    soe.pop()
                    if not soe: # 쌍을 다 맞춘 경우
                        flag = -1
                else:
                    return False
        # 대괄호
        if arr[i] == '[' or arr[i] == ']':  
            if arr[i] == '[':
                dae.append('[')
                flag = 1 
            else:
                if dae and (flag == 1 or flag == -1):
                    dae.pop()
                    if not dae: # 쌍을 다 맞춘 경우
                        flag = -1
                else:
                    return False
    
    return not (soe or dae)


string_input = si().strip()

if isOk(string_input):
    tmp = 1
    res = 0
    for i in range(len(string_input)):
        if string_input[i] == '(':
            tmp = tmp * 2
        elif string_input[i] == '[':
            tmp = tmp * 3 

        elif string_input[i] == ')':
            if string_input[i-1] == '(':
                res += tmp
            tmp = tmp // 2
        elif string_input[i] == ']':
            if string_input[i-1] == '[':
                res += tmp
            tmp = tmp // 3
    print(res)
else:
    print(0)