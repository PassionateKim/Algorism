# 2022-08-16
# 2022-08-17
# 2022-08-19
# 순위검색
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations
def solution(information, queries):
    answer = []
    candidate_dict = defaultdict(list)
    # 1. information을 dict에 다 넣기
    for info in information:
        info = info.split()
        key_list = info[:-1]
        score = int(info[-1])
        
        for i in range(5):
            combi_list = list(combinations([0,1,2,3], i)) # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]        
            for combi in combi_list: # [0, 1] in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
                tmp = key_list[:]
                print("combi:",combi)
                for idx in combi: # 0, 1
                    tmp[idx] = '-'
            
                candidate_dict["".join(tmp)].append(score)

    # 2. 정렬
    for value in candidate_dict.values():
        value.sort() 
                    
    # 3. 체크하기
    for query in queries:
        query = query.replace('and','')
        query = query.split()
        key = "".join(query[:-1])
        score = int(query[-1])
        
        count = 0
        if key in candidate_dict.keys():
            count = len(candidate_dict[key]) - bisect_left(candidate_dict[key], score)

        answer.append(count)
    print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])