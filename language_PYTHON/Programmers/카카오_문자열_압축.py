# 2022-06-06
# 2022-07-29
# 2022-07-30
# 문자열 압축
def solution(s):
    result = 1000
    # 1. 문자열 자르는 개수
    for i in range(1, len(s) + 1):
        tmp = s[0:i]
        cnt = 1
        answer = ""
        # 2. 문자열 탐색
        for j in range(i, len(s), i):
            string = s[j:j+i]
            
            # 다른 경우
            if tmp != string:
                if cnt > 1:
                    answer += str(cnt)
                answer += tmp

                # 초기화
                tmp = string
                cnt = 1
            # 같은 경우 
            else:
                cnt += 1


        # 3. 나머지 체크
        if cnt > 1:
            answer += str(cnt)
        answer += tmp
        result = min(result, len(answer))
    # /1.
    
    
    return result

solution("ababab")