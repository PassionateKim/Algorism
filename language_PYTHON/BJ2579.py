# 계단 오르기
N = int(input())
score_list = [int(input()) for _ in range(N)]

dp = [0] * (N+1)

for i in range(1, N+1):
    
    if i == 1: # i-1 은 인덱스때매 하나 빼준거뿐임
        dp[i] = score_list[i-1]
    elif i == 2:
        dp[i] = dp[1] + score_list[i-1]
    elif i == 3:
        dp[i] = max(score_list[i-3], score_list[i-2]) + score_list[i-1]
    else: # i >= 4 
        dp[i] = max(dp[i-2], dp[i-3] + score_list[i-2]) + score_list[i-1]
    

print(dp)