# 순위검색
# 복습 횟수:4, 00:45:00, 복습필요X
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    # 미리 만들고 시작하기
    info_dict = defaultdict(list)

    for info in information:
        info = info.split()
        
        for cnt in range(5):
            combi_s = list(combinations(range(4), cnt))
            for combi in combi_s:
                key = ""
                if 0 in combi:
                    key += info[0]
                else:
                    key += '-'

                if 1 in combi:
                    key += info[1]
                else:
                    key += '-'

                if 2 in combi:
                    key += info[2]
                else:
                    key += '-'

                if 3 in combi:
                    key += info[3]
                else:
                    key += '-'
                
                info_dict[key].append(int(info[4]))              

    for value in info_dict.values():
        value.sort()
    
    
    # query 판단하기
    for query in queries:
        query = query.split()
        score = int(query[-1])

        key = ""
        for i in range(0, len(query), 2):
            key += query[i]
        
        val = info_dict[key]

        idx = bisect_left(val, score)
        answer.append(len(val) - idx)
    
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])