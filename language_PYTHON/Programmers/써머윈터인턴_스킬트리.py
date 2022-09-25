# 2022-09-25
# 스킬 트리
def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    tmp_list = []
    # 완전탐색 순서가 있어야하므로 list
    for skill in skill_trees:
        skill = list(skill)
        tmp = []
        # skill_list에 있는 원소만 추출하기
        for s in skill:
            if s in skill_list:
                tmp.append(s)
        tmp_list.append(tmp)
    
    for tmp in tmp_list:
        flag = 1
        for i in range(len(tmp)):
            if tmp[i] != skill_list[i]: 
                flag = 0
        if flag:
            answer += 1
    print(answer)
         

    

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])