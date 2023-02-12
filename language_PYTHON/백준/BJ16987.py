# 계란으로 계란치기
# 복습 횟수:1, 00:45:00, 복습필요O
import sys
si = sys.stdin.readline
N = int(si())
eggs = [list(map(int, si().split())) for i in range(N)]
answer = 0

def dfs(index, eggs):
    global answer
    if index == len(eggs):
        cnt = 0
    
        for egg in eggs:
            if egg[0] <= 0:
                cnt += 1
        
        answer = max(answer, cnt)
        return

    if eggs[index][0] <= 0:
        dfs(index+1, eggs)
    else:
        is_all_broken = True
        for i in range(len(eggs)):
            if i != index and eggs[i][0] > 0:
                is_all_broken = False
                eggs[index][0] -= eggs[i][1]
                eggs[i][0] -= eggs[index][1]

                dfs(index+1, eggs)
                
                eggs[index][0] += eggs[i][1]
                eggs[i][0] += eggs[index][1]
                
        if is_all_broken:
            dfs(len(eggs), eggs)


dfs(0, eggs)
print(answer)