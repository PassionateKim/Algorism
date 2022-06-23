# 어두운 굴다리
import sys
si = sys.stdin.readline

N = int(si())
M = int(si())
location = list(map(int, si().split())) # 오름차순이라 sorted 안해도됨

def determination(distance, height):
    end_point = 0

    for i in range(len(location)):
        # 왼쪽
        if location[i] - height <= end_point:
            end_point = location[i] + height
        else:
            return False

    # distance를 모두 덮는 경우
    if end_point >= distance:
        return True    
    else:
        return False

def Binary(start, end):
    ans = N
    while start<=end:
        mid = (start+end)//2

        if determination(N, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

answer = Binary(1, int(1e8))
print(answer)