# 퇴사
import sys
si = sys.stdin.readline

N = int(si())
Ti = ['#'] + list() # 3  5  1  1  2  4   2
Pi = ['#'] + list() # 10 20 10 20 15 40 200
for i in range(N):
    t, p = list(map(int, si().split()))
    Ti.append(t)
    Pi.append(p)

maxi = -1e9 
def dfs(date, sum, tmp):
    global maxi
    if date > N+1:
        sum -= tmp
        maxi = max(maxi, sum)
        return
    if date == N+1:
        maxi = max(maxi, sum)
        return

    sum += Pi[date]
    # 그 자리 탐색
    dfs(date + Ti[date], sum, Pi[date])
    # 그 자리 탐색X
    dfs(date + 1, sum - Pi[date], Pi[date])

    return
# 날짜는 1일부터 시작
dfs(1, 0, 0)
print(maxi)