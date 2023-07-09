# 복습 횟수:0, 00:10:00, 복습필요X
import sys
si = sys.stdin.readline

N = int(si())
myset = set()

li = list(map(int, si().split()))
for elem in li:
    myset.add(elem)

print(len(myset))