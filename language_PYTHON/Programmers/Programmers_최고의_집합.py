# 복습 횟수:0, 00:30:00, 복습필요X
def solution(n, s):
    answer = []
    if n > s: return -1

    div = s // n
    rest = s % n

    for i in range(n):
        answer.append(div)
    
    for i in range(rest):
        answer[i] += 1
    
    answer.sort()

    return answer


print(solution(3, 8))