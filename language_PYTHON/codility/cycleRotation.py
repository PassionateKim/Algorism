# 복습 횟수:0, 00:15:00, 복습필요X
from collections import deque
def solution(A, K):
    a = deque(A)

    for i in range(K):
        if(len(a) != 0):
            tmp = a.pop()
            a.appendleft(tmp)
        

    return list(a)

solution([], 3)
