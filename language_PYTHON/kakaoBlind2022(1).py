#신고결과받기
from collections import defaultdict
import numbers


def solution(id_list, report, k):
    answer = [0] *len(id_list)
    
    report = set(report)

    user_list_i_reported = defaultdict(set)
    num_of_reported = defaultdict(int)
    suspended = []

    for r in report:
        report,be_reported = r.split()
        num_of_reported[be_reported] +=  1
        user_list_i_reported[report].add(be_reported)

        if(num_of_reported[be_reported] == k):
            suspended.append(be_reported)


    print(suspended)
    
            


    print(user_list_i_reported)
    return answer 
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)