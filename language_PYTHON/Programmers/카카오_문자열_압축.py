# 2022-06-06
# 2022-07-29
# 2022-07-30
# 2022-08-01
# 2022-08-05
# 2022-08-12
# 문자열 압축
def solution(s):
    answer = 1000
    for i in range(1, len(s) + 1):
        # cut의 범위
        buffer = ""
        tmp = s[:i]
        cnt = 1
        # 일단 string 자체로는 전범위를 탐색 가능하다.
        for j in range(i, len(s), i):
            string = s[j:j+i]
            if tmp == string:
                cnt += 1
            else:
                if cnt > 1:
                    buffer += str(cnt)
                buffer += tmp
                # 초기화
                tmp = string
                cnt = 1 
        if cnt > 1:
            buffer += str(cnt)
        buffer += tmp
        answer = min(answer, len(buffer))

    print(answer)    
    return answer
solution("aabbaccc")