# 신규 아이디 추천
def solution(new_id):
    answer = ''

    # 1단계
    answer = new_id.lower()
    
    # 2단계
    for i in answer:
        if i.islower() or i.isdigit() or i in "-_.":
            pass
        else:
            answer = answer.replace(i,"",1)

    # 3단계
    check = answer[:1]
    compare_string = answer[1:]

    for string in compare_string:
        if check[-1] == '.':
            if string == '.':
                pass
            else:
                check += string
        else:
            check += string
    print(check)
    
    # 4단계
    if answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 1:
        if answer[-1] == ".":
            answer = answer[:-1]
    
    # 5단계
    if len(answer) < 1:
        answer += 'a'
    
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        tmp = answer[-1]
        while True:
            answer += tmp
            if len(answer) == 3:
                break

    return answer

solution("...!@BaT#*..y.abcdefghijklm")