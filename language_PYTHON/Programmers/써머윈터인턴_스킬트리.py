# 2022-09-25
# 2024-05-09
# 스킬 트리
def solution(skill, skill_trees):
    answer = 0
    skill_sequence = skill
    
    for skill in skill_trees:
        cursor = 0
        is_true = True
        for val in skill:

            if val not in skill_sequence:
                continue
            if val == skill_sequence[cursor]:
                cursor += 1
            else:
                is_true = False
                break
        
        if is_true:
            answer += 1

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])