#동전 0


N,K = map(int,input().split())
count = 0
num = 0
coins_list = []
for i in range(N):
    coins_list.append(int(input()))

coins_list.sort(reverse=True)
answer = []
for coin in coins_list:
    if(coin <= K):
        count = count + K//coin
        K = K % coin

print(count)

    


