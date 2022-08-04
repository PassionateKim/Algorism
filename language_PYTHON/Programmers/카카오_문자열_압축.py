# 2022-06-06
# 2022-07-29
# 2022-07-30
# 2022-08-01
# 2022-08-05
# 문자열 압축
def solution(s):
    answer = 1000

    for i in range(1, len(s) + 1):
        i = len(s)
        tmp = s[:i]
        result = 0
        cnt = 1
        tmp_str = ""
        for j in range(i, len(s), i):
            string = s[j:j+i]

            if string != tmp:
                if cnt > 1:
                    tmp_str += str(cnt)
                tmp_str += tmp

                # 초기화
                tmp = string
                cnt = 1
            else:
                cnt += 1
        
        # 끝
        if cnt > 1:
            tmp_str += str(cnt)
        tmp_str += tmp
        answer = min(answer, len(tmp_str))

    return answer
solution("aabbaccc")