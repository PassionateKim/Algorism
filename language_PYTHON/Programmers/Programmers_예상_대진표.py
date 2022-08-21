# 2022-08-21
# 예상 대진표
def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        # 1. check 반례: 8,4,5 
        maxi, mini = max(a, b), min(a, b)
        # 최대값이 짝수이고, 최대값-1 == 최솟값인 경우
        if maxi % 2 == 0 and maxi - 1 == mini:
            break

        # 2. 홀 짝 체크
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
        
        a //= 2
        b //= 2

    return answer

print(solution(8,4,7))