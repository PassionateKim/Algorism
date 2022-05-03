# 보물
import sys
N = int(input())

A_array = list(map(int, sys.stdin.readline().rstrip().split()))
B_array = list(map(int, sys.stdin.readline().rstrip().split()))

A_array = sorted(A_array)
B_array = list(reversed(sorted(B_array)))

sum  = 0

for i in range(N):
    sum += A_array[i] * B_array[i]

print(sum)