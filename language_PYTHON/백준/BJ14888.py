#연산자 끼워넣기
# 복습 횟수:3, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
maxi = -1 * sys.maxsize
mini = sys.maxsize

N = int(si())
li = list(map(int, si().split()))
# 덧셈, 뺼셈, 곱셈, 나눗셈
oper_list = list(map(int, si().split()))

def dfs(index, sumi):
    global maxi
    global mini
    if index == N:
        maxi = max(maxi, sumi)
        mini = min(mini, sumi) 
        return
    
    if oper_list[0]:
        oper_list[0] -= 1
        dfs(index + 1, sumi + li[index])
        oper_list[0] += 1
    
    if oper_list[1]:
        oper_list[1] -= 1
        dfs(index + 1, sumi - li[index])
        oper_list[1] += 1
    
    
    if oper_list[2]:
        oper_list[2] -= 1
        dfs(index + 1, sumi * li[index])
        oper_list[2] += 1

    if oper_list[3]:
        oper_list[3] -= 1
        if sumi < 0:
            tmp = (-sumi) // li[index]
            tmp = -tmp
        else:
            tmp = sumi // li[index]
        dfs(index + 1, tmp)
        oper_list[3] += 1

dfs(1, li[0])
print(maxi)
print(mini)