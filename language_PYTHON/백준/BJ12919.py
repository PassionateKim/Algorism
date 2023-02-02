# A와 B 2
# 복습 횟수:1, 00:45:00, 복습필요O
# == 시간초과 코드 == #
import sys
si = sys.stdin.readline
S = list(map(str, si().rstrip()))
T = list(map(str, si().rstrip()))

def dfs(S: list):
    if len(S) == len(T):
        if S == T:
            print(1)
            exit()
        else: return
    
    S.append('A')
    dfs(S)
    S.pop() # 원상 복구
    
    S.append('B')
    S.reverse()
    dfs(S)
    S.pop(0) # 원상 복구
    S.reverse() 

dfs(S)
print(0)

# == 정답 코드 == #
import sys
si = sys.stdin.readline
S = list(map(str, si().rstrip()))
T = list(map(str, si().rstrip()))

def dfs(T: list):
    if S == T: 
        print(1)
        exit()

    if len(T) <= len(S): return

    if T[-1] == 'A':
        dfs(T[:-1]) # A를 뺸다

    if T[0] == 'B':
        dfs(list(reversed(T[1:])))

dfs(T)
print(0)