# 신규 아이디 추천
N = input()
a = "hello"

def solution(new_id):
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    for i in answer:
        if "a" <= i <= "z" or i.isdigit() or i == '-' or i == '_' or i == '.':
            continue
        answer = answer.replace(i,"")
    
    # 3단계
    while ".." in answer:
        answer = answer.replace("..",".")
        
    # 4단계
    if len(answer) > 1 and answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]

    return answer


print(solution(N))