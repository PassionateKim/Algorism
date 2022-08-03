# 2022-06-08
# 2022-08-03
# 메뉴 리뉴얼
from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    answer = []
    # course
    for cnt in course:
        candidate_dict = defaultdict(int)
        for od in orders:
            # list로 바꾸기
            food_list = list(map(str, od))
            combi = list(combinations(food_list, cnt))
            for c in combi: # ("A", "B")
                
                candi = "".join(sorted(c))
                
                if candi in candidate_dict.keys():
                    candidate_dict[candi] += 1
                else:
                    candidate_dict[candi] = 1

        
            # /od
        # /cnt
        print(candidate_dict.items())
        if candidate_dict:
            maxi = max(candidate_dict.values())
            for key, value in candidate_dict.items():
                if value == maxi and maxi != 1:
                    answer.append(key)

    answer.sort()
    print(answer)
    return answer

solution(["XYZ", "XWY", "WXA"],[2,3,4])
# solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])

# set.add
# set, dict 는 in 체크할때 해쉬를 사용해 O(1)