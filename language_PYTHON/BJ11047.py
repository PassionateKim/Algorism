#동전 0
from ast import Return


N,K = map(int,input().split())
count = 0
num = 0
coins_list = []
for i in range(N):
    coins_list.append(int(input()))

coins_list.sort()
answer = []
while True:
    num = num + coins_list[N-1]
    if(num > K):
        num = num - coins_list[N-1]
        N = N -1
    elif(num < K):
        count += 1
        #정답 체크용
        answer.append(coins_list[N-1])
        continue
    
    elif(num == K):
        count+=1
        answer.append(coins_list[N-1])
        print(count,answer)
        break

    


