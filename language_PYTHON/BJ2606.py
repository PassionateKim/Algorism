#바이러스
N = int(input())
M = int(input())
#1포함
count = 1

computer_list = [[] for i in range(N+1)]
visited = [False] *(N+1)
visited[1] = True
for i in range(M):
    a,b = map(int,input().split())
    computer_list[a].append(b)
    computer_list[b].append(a)

for i in range(1,N+1):
    computer_list[i].sort()

print(computer_list)

def dfs(idx):
    global count
    
    for i in computer_list[idx]:
        if not visited[i]:
            count += 1
            visited[i] = True 
            dfs(i)




dfs(1)
print(count)