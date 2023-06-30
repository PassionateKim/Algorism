# 복습 횟수:0, 00:15:00, 복습필요X
def solution(A: list, B: list):
    answer = 0
    A.sort()
    B.sort(reverse=True)
   
    
    for a, b in zip(A, B):
        answer += a * b

    return answer

solution([1, 4, 5, 2, 3], [5, 3, 2, 1, 7])