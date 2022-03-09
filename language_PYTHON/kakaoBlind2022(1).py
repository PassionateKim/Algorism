#신고결과받기
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
    print(reports)
    print(id_list)
    for r in set(report):    
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
            print(r.split()[0],answer)

    return answer

# def solution(id_list, report, k):
#     answer = [0] *len(id_list)
    
#     report = set(report)

#     user_list_i_reported = defaultdict(set)
#     num_of_reported = defaultdict(int)
#     prosecuted = []

#     for r in report:
#         report,be_reported = r.split()
#         num_of_reported[be_reported] +=  1
#         user_list_i_reported[report].add(be_reported)

#         if(num_of_reported[be_reported] == k):
#             prosecuted.append(be_reported)


    
    
            
#     print(user_list_i_reported)

#     for target in prosecuted:
#         for i in range(len(id_list)):
#             if (target in user_list_i_reported[id_list[i]]):
#                 answer[i] += 1
#     return answer 
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)