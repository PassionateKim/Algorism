#카드 2
from collections import deque
card_array = deque()
N = int(input())

for i in range(1,N+1):
    card_array.append(i)

while len(card_array) > 1:
    card_array.popleft()
    a = card_array.popleft()
    card_array.append(a)

print(*card_array)

