# 용돈 관리
# 이분탐색 -> 인출금액 k 최소화
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
A = []
for i in range(N):
    A.append(int(si()))


def determination(array, mid, target):
    # 돈을 넣은 채로 시작
    cnt = 1
    in_pocket = mid
    for i in array:
        if in_pocket >= i:
            in_pocket -= i
        else:
            cnt += 1 # 주머니에서 돈 꺼내기
            in_pocket = mid - i # 사용
            
    return cnt <= target

def Binary(array, start, end, target):
    ans = 0
    while start<=end:
        mid = (start + end) // 2
        
        if determination(array, mid, target):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1 
    return ans

print(Binary(A, max(A), int(1e6), M))