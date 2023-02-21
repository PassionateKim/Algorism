from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    callie_dict = defaultdict(list)
    report_dict = dict()
    report_set = set(report) # 중복 제외를 위해 set 사용

    for report in report_set:
        caller, collie = map(str, report.split())
        
        callie_dict[caller].append(collie)
        
        if collie in report_dict.keys():
            report_dict[collie] += 1
        else:
            report_dict[collie] = 1
        
    target_list = []
    for key, value in report_dict.items():
        if value >= k:
            target_list.append(key)
    
    for id in id_list:
        if callie_dict[id]:
            tmp = 0
            for callie in callie_dict[id]:
                if callie in target_list:
                    tmp += 1
            answer.append(tmp)
        else:
            answer.append(0)

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)