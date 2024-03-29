import sys
si = sys.stdin.readline 

N, M = map(int, si().split())
arr = list(map(int, si().split()))
mud_dict = dict()

for i in range(M):
    x, y, k = map(int, si().split()) 
    x, y = x-1, y-1

    mud_dict[x] = mud_dict.get(x, 0) + k
    mud_dict[y + 1] = mud_dict.get(y + 1, 0) - k

answer = []
prefix_sum = 0
for index, val in enumerate(arr):
    prefix_sum = prefix_sum + mud_dict.get(index, 0)
    answer.append(arr[index] + prefix_sum)

print(*answer)