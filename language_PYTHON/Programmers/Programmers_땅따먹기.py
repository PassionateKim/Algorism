def solution(land):
    answer = 0
    
    dp = [[0, 0, 0, 0] for i in range(len(land))]
    dp[0] = land[0]

    for i in range(len(land) - 1):
        dp[i + 1][0] = max(dp[i][1], dp[i][2], dp[i][3]) + land[i + 1][0]
        dp[i + 1][1] = max(dp[i][0], dp[i][2], dp[i][3]) + land[i + 1][1]
        dp[i + 1][2] = max(dp[i][0], dp[i][1], dp[i][3]) + land[i + 1][2]
        dp[i + 1][3] = max(dp[i][0], dp[i][1], dp[i][2]) + land[i + 1][3]
        

    answer = max(dp[-1])
    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]	)