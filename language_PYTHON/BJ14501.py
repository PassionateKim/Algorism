# 퇴사
N = int(input())
schedule_list = [list(map(int, input().split())) for _ in range(N)]
answer_list = []
# 백트레킹으로 풀어야할 거같은데

def dfs(sum, day):
    answer_list.append(sum) 
  
    

    for i in range(day, N):
        tmp = i + schedule_list[i][0] # 다음회차에 가능한지 체크
        if i + schedule_list[i][0] <= N: 
            dfs(sum + schedule_list[i][1] , i + schedule_list[i][0])
        
dfs(0,0)
print(max(answer_list))