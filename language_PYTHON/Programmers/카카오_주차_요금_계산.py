# 주차 요금 계산
# 복습 횟수:1, 01:00:00, 복습필요O
import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    car_set = set()
    car_dict = defaultdict(list)
    # 기본 시간(분) # 기본 요금 # 단위 시간 # 단위 요금
    for info in records:
        time, number, in_out = map(str, info.split())
        time = (int(time.split(":")[0]) * 60) + int(time.split(":")[1])

        # car 넣기 - for sort
        car_set.add(number)
        car_list = list(car_set)
        car_list.sort()

        if car_dict[number]:
            tmp = time - car_dict[number][0]
            answer.append([number, tmp])
            car_dict[number].pop()
        else:
            car_dict[number].append(time)    
    
    for key, value in car_dict.items():
        if len(value) == 1:
            answer.append([key, 23*60 + 59 - value[0]]) 
    
    # 계산하기
    time_list = [0] * len(car_list)
    for val in answer:
        index = car_list.index(val[0])
        time_list[index] += val[1]
    result = []

    for time in time_list:
        if time <= fees[0]: #기본시간보다 작거나 같은 경우
            result.append(fees[1])
        else:
            diff_t = time - fees[0]
            diff_fee = math.ceil((diff_t / fees[2])) * fees[3]
            result.append(fees[1] + diff_fee) 
    return result

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])