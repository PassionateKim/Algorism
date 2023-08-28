# 주차 요금 계산
# 복습 횟수:2, 01:00:00, 복습필요X
import math

def solution(fees, records):
    answer = []
    result_sum_dict = dict()
    check_car_dict = dict()

    # 세기 위한 dict 초기화
    for record in records:
        time, car_num, in_out = record.split(" ")
        if car_num not in result_sum_dict:
            result_sum_dict[car_num] = 0

    # dict 체크
    for record in records:
        time, car_num, in_out = record.split(" ")
        if car_num not in check_car_dict:
            check_car_dict[car_num] = time
        else: # 이미 있는 경우
            exist_time = check_car_dict[car_num]
            exist_time = int(exist_time.split(":")[0]) * 60 + int(exist_time.split(":")[1])
            later_time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])

            time_diff = later_time - exist_time
            # 더하기
            result_sum_dict[car_num] += time_diff
            del check_car_dict[car_num]
            

    # 남은 거 체크
    for car_num, time in check_car_dict.items():
        later_time = 23 * 60 + 59
        exist_time = check_car_dict[car_num]
        exist_time = int(exist_time.split(":")[0]) * 60 + int(exist_time.split(":")[1])
        
        time_diff = later_time - exist_time
        
        # 더하기
        result_sum_dict[car_num] += time_diff
            


    sorted_dict = sorted(result_sum_dict.items())
    for key, value in sorted_dict:
        if value <= fees[0]: # 기본시간 이내라면
            answer.append(fees[1])
        else:
            time_diff = value - fees[0]
            left_fee= math.ceil(time_diff / fees[2]) * fees[3]
            answer.append(fees[1] + left_fee)

    return answer

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	))

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])