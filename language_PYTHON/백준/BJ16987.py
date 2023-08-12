# 계란으로 계란치기
# 복습 횟수:2, 00:45:00, 복습필요2
import sys
si = sys.stdin.readline
N = int(si())
egg_list = []

for i in range(N):
    shield, weight = map(int, si().split())
    egg_list.append([shield, weight])

answer = 0
def dfs(egg_index):
    global answer
    if egg_index == len(egg_list):
        candidate = 0
        
        for shield, weight in egg_list:
            if shield <= 0:
                candidate += 1
        
        answer = max(answer, candidate)
        return

    current_egg_shield, current_egg_weight = egg_list[egg_index]
    if current_egg_shield <= 0: # 손에 든 계란이 꺠진 경우
        dfs(egg_index + 1) # 그냥 넘어간다
    else:
        is_all_broken = True
        for i in range(len(egg_list)):
            if i == egg_index or egg_list[i][0] <= 0: continue # 같은 것끼리 깰 순 없으므로
            
            is_all_broken = False

            target_egg_shield, target_egg_weight = egg_list[i]
            # if target_egg_shield <= 0: # target이 깨진 경우
                # dfs(egg_index + 1) # 그냥 넘어간다.
                # 서로 꺤다
            egg_list[egg_index][0] -= target_egg_weight
            egg_list[i][0] -= current_egg_weight
            
            dfs(egg_index + 1)

            # reset
            egg_list[egg_index][0] += target_egg_weight
            egg_list[i][0] += current_egg_weight

        if is_all_broken:
            dfs(len(egg_list))    
    return

dfs(0)
print(answer)