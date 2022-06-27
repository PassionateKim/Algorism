# 어두운 굴다리
import sys
si = sys.stdin.readline

N = int(si())
M = int(si())
location = list(map(int, si().split())) # 오름차순이라 sorted 안해도됨

def determination(garosu, height):
    end_point = 0
    for ga in garosu:
        if ga - height <= end_point: # 좌
            end_point = ga + height # 우
        else:
            return False
    return end_point >= N

def Binary(start, end, garosu):
    ans = 0
    while start<=end:
        mid = (start + end) // 2
        if determination(garosu, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1


    return ans

print(Binary(1, N, location))