# 텀 프로젝트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# dfs 풀이

def dfs(x):
    global cycle
    
    visited[x] = 1 # 방문처리
    temp_cycle.append(x)
    num = arr[x]

    if visited[num] == 1:
        if num in temp_cycle:
            cycle += temp_cycle[temp_cycle.index(num):]
        return
    else:
        dfs(num)


T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    cycle = []

    for i in range(1, N+1):
        if visited[i] == 0: 
            temp_cycle = []
            dfs(i)
    
    print(N - len(cycle))





# 풀이 2
# T = int(input().rstrip())
# for _ in range(T):
#     N = int(input().rstrip())
#     p = [0] + list(map(int, input().split()))
#     team = [0] * (N+1)

#     for i in range(1, N+1):
#         if team[i] == 0: # 팀이 없는 경우
#             team_number = i
#             # 팀 구성한다고 가정하기
#             while team[i] == 0:
#                 team[i] = team_number # 내 풀이와의 차이 1이 아니라 team_num
#                 i = p[i]
#             # 역순으로 순환하며 사이클 확인
#             while team[i] == team_number:
#                 team[i] = -1
#                 i = p[i]
#     result = N - team.count(-1)
#     print(result)
 




# 틀린 풀이
# 1. 반례 2 3 4 5 6 2 
# for i in range(int(input().rstrip())):
#     # 초기화
#     student_num = int(input().rstrip())
#     student_list = [0] + list(map(int, input().split()))
#     student_who_has_team = []
#     visited = [0] * len(student_list)

#     for i in range(1, len(student_list)):
#         start = i
#         team_member = [start] # 팀 멤버 구성하는 애들 체크
#         visited[start] = 1 # 방문처리
#         q = deque() # 아래의 while 때문에 없어도 되지만, 초기화라는 점에서 넣어둔 코드
#         q.append(student_list[i]) 
              
#         while q:
#             end = q.popleft() 
#             if end == start: # 꼬리물기 되는 경우
#                 student_who_has_team.extend(team_member)
#                 break

#             if visited[end] == 0:  # 방문하지 않은 경우
#                 q.append(student_list[end]) 
#                 team_member.append(end)
#                 visited[end] = 1
    
#     print((len(student_list)-1) - len(student_who_has_team)) # 편의를 위해 임의로 len을 1늘렸었으므로, 다시 뺴줌

