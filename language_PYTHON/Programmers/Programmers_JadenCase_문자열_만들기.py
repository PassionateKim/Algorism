# 2022-09-09
# 2022-09-10
# JadenCase 문자열 만들기
def solution(ss):
    answer = ''
    ss = ss.split(" ")
    for s in ss:
        # 일반일때
        
        # 공백일 때
        if s == '':
            answer += ' '
        else:
            tmp = ''
            for i in range(len(s)):
                if i == 0:
                    tmp += s[i].upper()
                else:
                    tmp += s[i].lower()    
            answer += tmp +' ' 

    return answer

print(solution("3people unFollowed me"))
# s=s.split(" ") 자르기 참고