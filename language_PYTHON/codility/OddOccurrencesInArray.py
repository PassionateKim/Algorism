# 복습 횟수:0, 00:15:00, 복습필요X
from collections import defaultdict

def solution(A):
    dict_ = defaultdict(int)
    
    for i in range(len(A)):
        val = A[i]
        if(val in dict_.keys()):
            dict_[val] = dict_[val] + 1
        else:
            dict_[val] = 1



    for key, value in dict_.items():
        if (value % 2):
            return key

print(solution([9, 3, 9, 3, 9, 7, 9]))