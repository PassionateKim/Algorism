# 최소, 최대 2
import sys
si = sys.stdin.readline

N = int(si())
for i in range(N*2):
    a = list(map(int, si().split()))

    if  i % 2 == 1:
        print(min(a),max(a))