# 복습 횟수:0, 00:45:00, 복습 필요X
import math
def solution(n, stations, w):
    answer = 0
    dist = []
    # 중간의 남은 지점
    for i in range(1, len(stations)):
        right = stations[i] - w
        left = stations[i-1] + w
        dist.append(right - left - 1)
    
    # 맨 앞
    dist.append(stations[0] - w - 1)
    # 맨 뒤
    dist.append(n - (stations[-1] + w))
    
    for d in dist:
        if d <= 0: continue

        answer += (math.ceil(d / (2*w + 1)))
    return answer

solution(11, [4, 11], 1)