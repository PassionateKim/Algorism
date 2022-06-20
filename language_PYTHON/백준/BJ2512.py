# 예산
import sys
si = sys.stdin.readline

N = int(si())
A = list(map(int, si().split()))
maxi = int(si())

# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
if sum(A) <= maxi:
    print(max(A))
    exit()

# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

def Binary(array, start, end, target):
    answer = 0
    while start<=end:
        mid = (start+end)//2
        
        sumi = 0
        for i in array:
            if i >= mid:
                sumi += mid
            else:
                sumi += i

        if sumi <= target:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

print(Binary(A, 1, max(A), maxi))