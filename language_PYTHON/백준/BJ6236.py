# 용돈 관리
# 이분탐색 -> 인출금액 k 최소화
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
A = []
for i in range(N):
    A.append(int(si()))

# 인출금액 뽑기
def determination(k):
    # 뽑은 상태에서 시작
    cnt = 1
    coin = k
    for i in A:
        # 돈이 부족한 경우
        if coin - i < 0:
            cnt += 1
            coin = k
        # 돈이 여유로운 경우
        else:
            coin -= i
    # 작기만 하면 인출해서 맞추면 되므로 <= 부등호
    return cnt <= M

start, end, ans = max(A), 1000000000, 0
while start<=end:
    mid = (start+end)//2
    if determination(mid):
        ans = mid
        end = mid - 1
    else:
        start = mid + 1 

print(ans)