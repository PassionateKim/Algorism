# 2022-09-09
# JadenCase 문자열 만들기
def solution(ss):
    blank_list = []
    
    i = 0
    while i < len(ss):
        if ss[i] == ' ':
            cnt = 1
            i += 1
            while i < len(ss) and ss[i] == ' ':
                cnt += 1
                i += 1
            blank_list.append(cnt)
        i += 1
    answer = ''
    ss = ss.split()
    new_ss = []
    # 1. 2차원 배열로 넣기 -> string은 바꿀 수 없음
    for s in ss:
        s = list(s)
        new_ss.append(s)
    # 2. 변환하기
    for string in new_ss:
        for i in range(len(string)):
            if i == 0:
                if string[i].isalpha():
                    string[i] = string[i].upper()
            else:
                if string[i].isalpha():
                    string[i] = string[i].lower()
    
    # 3 answer을 다시 string으로 바꾸기
    for i in range(len(new_ss) + len(blank_list)):
        if i % 2 == 0:
            answer += "".join(new_ss[i//2])
        else:
            answer += (" " * blank_list[i//2])

    return answer

print(solution("people Aws   3   "))