# 멀쩡한 사각형
import math

def solution(w,h):
    cnt = 0
    total = int(w*h)
    y = w / h  # 기울기
    print(y)
    for i in range(h):
        start = (y * i)
        end = (y * (i+1))
        
        # 시작점이 정수일 때
        if start == int(start):
            # 정수
            if end == int(end):
                # print(end - start)
                cnt += end - start
            # 정수 X
            else:
                cnt += math.trunc(end - start) + 1
        # 시작점이 정수X 일 때
        else:
            # 정수
            if end == int(end):
                cnt += math.trunc(end - start) + 1
            # 정수 X
            else:
                #  + 정수 격차 
                cnt += (math.trunc(end) - math.trunc(start)) + 1
    return total-cnt
solution(8,12)