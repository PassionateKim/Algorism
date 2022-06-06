#문자열 압축
# 압축 최대 lengh의 반
# 빼고 뺸 게 작으면 break 
def solution(s):
    min_num = len(s)
    for i in range(1, len(s)//2+1):
        cnt = 1
        left_line, right_line, tmp = s[:i], s[i:], ""
        while True:
            if len(right_line) < i: # 문자열을 다 돌게 된 경우
                break

            if left_line == right_line[:i]:
                right_line = right_line.replace(left_line,"",1)
                cnt += 1
            else: # 다를 때
                if cnt != 1:
                    tmp += str(cnt) + left_line
                elif cnt == 1:
                    tmp += left_line
                cnt = 1 # 초기화
                left_line = right_line[:i]
                right_line = right_line.replace(left_line,"",1)

        if cnt != 1:
            tmp += str(cnt) + left_line + right_line
        else:
            tmp += left_line + right_line

        min_num = min(len(tmp), min_num)
    
    return min_num


solution("a")