# 1,2,3 더하기
T = int(input())

def bfs(sum, depth):
    global cnt
    if sum == n: #탈출 조건
        cnt += 1
        return
    if depth >= n: # 나머지 안되는 do들 탈출
        return
    
    for i in range(1, 4):
        bfs(sum+i, depth+1)
        


for i in range(T):
    cnt = 0
    n = int(input())
    bfs(0,0)
    print(cnt)