# 2022-08-15
# 2022-08-16
# 후보키
from itertools import combinations


def solution(relation):
    
    n = len(relation)
    m = len(relation[0])
    combi = []
    tmp_key_len = [i for i in range(m)]
    
    # 1. 가능한 모든 후보키
    for i in range(1, m+1):
        combi += combinations(tmp_key_len, i)
    
    unique_key = set()

    # 2. 키에 따라 값 모두 체크하기
    for keys in combi:
        tmp_set = []
        # [0,1] 이라고 해보자.
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        print(tmp)
        exit()
        for item in relation:
            tmp = []
            # 키 모두 체크
            for key in keys:
                tmp.append(item[key])

            tmp_set.append(tuple(tmp))
        # 유일성
        if len(set(tmp_set)) == n:
            unique = True  
            # 최소성
            for x in unique_key:
                if set(x).issubset(set(keys)):
                    unique = False
                    break   

            if unique:
                unique_key.add(keys)

    return len(unique_key)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

# 틀린 이유
# tuple을 어떻게 구현할지 몰랐음 (안에서 list comprehension을 쓸 줄 몰랐음.)
# issubset을 몰랐음
# set 안에서 tuple은 hashable , list는 hashable X



