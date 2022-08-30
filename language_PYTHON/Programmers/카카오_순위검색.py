# 2022-08-16
# 2022-08-17
# 2022-08-19
# 2022-08-30
# 순위검색
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(information, queries):
    answer = []
    candidate_dict = defaultdict(list)
    # 1. candidate_dict 만들기
    for info in information:
        info = info.split()
        key_list = info[:-1]
        
        score = int(info[-1])

        c = [i for i in range(len(key_list))]
        for i in range(len(key_list) + 1):
            combi_list = list(combinations(c, i))
            for combi in combi_list:
                tmp = key_list[:]
                for idx in combi:
                    tmp[idx] = '-'
                candidate_dict["".join(tmp)].append(score)
    
    # 2. candidate_dict 정렬하기
    for value in candidate_dict.values():
        value.sort()
    
    # 3. 이분탐색으로 개수구하기
    for query in queries:
        query = query.replace("and","")
        query = query.split()
        key_list = query[:-1]
        key = "".join(key_list)
        score = int(query[-1])
        
        if key in candidate_dict.keys():
            count = 0
            val = len(candidate_dict[key]) - bisect_left(candidate_dict[key], score)
            print(val)
    exit()

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])