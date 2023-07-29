# 복습 횟수:1, 01:00:00, 복습필요O
def solution(n):
    answer = 0
    while(n != 0):
        if (n % 2 == 0):
            n = n // 2
        else:
            answer += 1
            n = n - 1

    return answer

print(solution(1000000000000000000))