#요세푸스 문제 0
from collections import deque

one = deque()
N,K = map(int,input().split())
answer = []

for i in range(1,N+1):
    one.append(i)



while len(one) >= 1:
    cnt = 0
    while cnt < K:
        one.append(one.popleft())
        cnt += 1
    answer.append(one.pop())
    if(len(one) == 1):
        answer.append(one.pop())

print("<",end="")
for i in range(len(answer)-1):
    print(answer[i],end=", ")
print(str(answer[-1])+">")