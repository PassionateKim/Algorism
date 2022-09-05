# 2022-08-15
# 2022-08-16
# 2022-09-05
# 후보키
from itertools import combinations


def solution(relations):
    answer = 0
    candidate_keySet = set()
    forComp = [i for i in range(len(relations[0]))]
    
    # 1. combi로 체크
    for i in range(1, len(forComp) + 1):
        combi_list = list(combinations(forComp, i))
        # 2. 행의 개수가 tmp_len의 개수와 일치하는지(일치하지않으면 중복이 있어서 유일성X)
        for combi in combi_list:
            candidate_tuple = combi
            tmp_len = len(relations)
            tmp_set = set()
            # 병렬로 체크 시작
            for relation in relations:
                tmp = []
                for i in candidate_tuple:
                    tmp.append(relation[i])
                tmp_set.add("".join(tmp))
            # 행의 개수가 tmp의 개수와 같지 않으면 유일성을 만족하지 않는다.
            if tmp_len != len(tmp_set): continue
            # 서브셋이면 최소성을 만족하지 않는다.
            flag = 1
            for s in candidate_keySet:
                if set(s).issubset(set(candidate_tuple)):
                    flag = 0
                    break
            
            if flag == 1:
                candidate_keySet.add(candidate_tuple)
                
    print(candidate_keySet)                    
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

# 틀린 이유
# tuple을 어떻게 구현할지 몰랐음 (안에서 list comprehension을 쓸 줄 몰랐음.)
# issubset을 몰랐음
# set 안에서 tuple은 hashable , list는 hashable X