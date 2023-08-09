# A와 B 2
# 복습 횟수:2, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline 
S = list(map(str, si().rstrip()))
T = list(map(str, si().rstrip()))


answer = 0 

def dfs(t: list):
    global answer
    if len(t) == 0:
        return
    
    if t == S:
        answer = 1
        return
    
    if t[-1] == 'A':
        t.pop()
        dfs(t)
        t.append('A')

    if t[0] == 'B':
        t.reverse()
        t.pop()
        dfs(t)
        t.append('B')
        t.reverse()

dfs(T)
print(answer)