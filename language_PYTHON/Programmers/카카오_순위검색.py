# 2022-08-16
# 2022-08-17
# 순위검색
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations
def solution(information, queries):
    answer = []
    answer_dict = defaultdict(list)
    # 1. 데이터 넣기
    for info in information:
        info = info.split()

        # 모두 dict에 저장해버리기
        # key_list와 score 구하기
        key_list = info[:-1]
        score = int(info[-1])
        
        # 그 외
        for i in range(5):
            combi = list(combinations([0,1,2,3], i))

            # combi 단위로 -로 바꿔서 dict에 담기
            for com in combi: #[(0,1,2), (1,2,3)]
                tmp = key_list[:]
                for j in com: #(0,1,2)
                    tmp[j] = '-'
                answer_dict["".join(tmp)].append(score) 
    
    # 2. 데이터 정렬 for 이분탐색
    for value in answer_dict.values():
        value.sort()
    
    # 3. 이분탐색으로 체크
    for query in queries:
        query = query.replace("and",'')
        query = query.split()
        condition = query[:-1]
        score = int(query[-1])
        key = "".join(condition)

        # 키가 있는 경우
        if key in answer_dict.keys():
            val = answer_dict[key] # list
            count = len(val) - bisect_left(val, score)
        answer.append(count)
    print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])