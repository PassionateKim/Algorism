# 계란으로 계란치기
# 복습 횟수:3, 00:45:00, 복습필요2
import sys
si = sys.stdin.readline 
N = int(si())
egg_list = []

for i in range(N):
    tmp = list(map(int, si().split()))
    egg_list.append(tmp)

answer = 0
def dfs(depth):
    global answer
    if depth == N:
        candidate = 0
        for i in range(N):
            if egg_list[i][0] <= 0:
                candidate += 1
        
        answer = max(answer, candidate)
        return

    if egg_list[depth][0] > 0: # 내구도가 있는 경우에만
        
        for i in range(N):
            if i != depth:
                if egg_list[i][0] > 0: # 내 계란이 아니고 깨려는 계란이 내구도가 있는 경우에는 깬다.
                    egg_list[depth][0] = egg_list[depth][0] - egg_list[i][1]
                    egg_list[i][0] = egg_list[i][0] - egg_list[depth][1]
                    
                    dfs(depth + 1)
                    # 원상복구
                    egg_list[depth][0] = egg_list[depth][0] + egg_list[i][1]
                    egg_list[i][0] = egg_list[i][0] + egg_list[depth][1]
                    
                else: # 그냥 간다
                    dfs(depth + 1)
    else:
        dfs(depth + 1)


    return

dfs(0)
print(answer)