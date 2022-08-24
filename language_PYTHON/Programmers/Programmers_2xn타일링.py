# 2022-08-24
# 2xn 타일링
def solution(n):
    answer = 0
    cnt = 0 
    # 2의 n-1승 OK
    # 사이사이 넣는 것?

    if n == 1:
        answer = 1
    # 홀 수 인 경우
    elif n % 2 != 0:
        val = n // 2 - 1
        cnt = 0
        answer = 3
        while cnt < val:
            answer *= 2
            answer = answer % 1000000007
            cnt += 1

    print(answer)
    return answer

solution(5)