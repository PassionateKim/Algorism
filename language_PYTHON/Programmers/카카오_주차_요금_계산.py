# 2022-09-14
# 주차 요금 계산
from collections import defaultdict
import math
def solution(fees, records):
    check_dict = defaultdict(list)
    answer = []
    standard_time, standard_fee, time, fee = fees[0], fees[1], fees[2], fees[3]
    print("기본 시간:",standard_time,"기본 요금:" , standard_fee,"단위 시간:",time,"단위 요금:", fee)
    # 1. dict 안에 담기
    for record in records:
        record = record.split()
        t, key, b = record[0], record[1], record[2]
        # t int -> 분으로 계산하기
        t = t.split(":")
        t = int(t[0]) * 60 + int(t[1])
        if b == 'IN':
            check_dict[key].append((-t, b))
        else:
            check_dict[key].append((t, b))
       
    # 2. 3개면 무조건 출차 내역이 없는 것이므로, 23:59에 출차된 것을 추가한다.
    for key, value in check_dict.items():
        if len(value) % 2 != 0:
            check_dict[key].append((1439,'OUT'))
    
    
    check_dict = sorted(check_dict.items())
    
    # 3. 각각의 주차 시간 구하기
    candidate = []
    for val in check_dict:
        sumi = 0
        for t in val[1]:
            sumi += t[0]
        candidate.append(sumi)
    
    # 주차 요금 계산하기
    for candi in candidate:
        # 주차 시간이 기본 시간보다 작거나 같은 경우
        if candi <= standard_time:
            answer.append(standard_fee)
        else:
            sumi = 0 + standard_fee
            diff_time = candi - standard_time
            q = math.ceil(diff_time/time)
            sumi += q * fee

            answer.append(sumi)
    print(answer)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])