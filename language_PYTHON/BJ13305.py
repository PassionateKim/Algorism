#주유소




N = int(input())
distance_list = list(map(int,input().split()))
oil_price_list = list(map(int,input().split()))

sum = 0
#2
distance = distance_list[0] 
price = oil_price_list[0]

for i in range(N-2):
    if(oil_price_list[i] <= oil_price_list[i+1]):
        distance += distance_list[i+1]
        oil_price_list[i+1] = oil_price_list[i] 
    else:
        #그전까지의 계산 정산
        sum = sum + distance * price
        #새로운 것으로 초기화
        distance = distance_list[i+1]
        price = oil_price_list[i+1]

print(sum+distance*price)
 

   




