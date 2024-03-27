import sys
si = sys.stdin.readline 
N, K = map(int, si().split())

arr = [0] + list(map(int, si().split()))

prefix = [0]

for i in range(1, N + 1):
    prefix.append(prefix[i-1] + arr[i])
 
cnt = dict()
answer = 0

for i in range(N + 1):
    answer = answer + cnt.get(prefix[i] - K, 0)

    if prefix[i] not in cnt:
        cnt[prefix[i]] = 1
    else:
        cnt[prefix[i]] = cnt[prefix[i]] + 1

print(answer)