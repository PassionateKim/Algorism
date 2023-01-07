# 숫자 빈도수
import sys
si = sys.stdin.readline

N, M = map(int, si().split())

check_list = []

for i in range(1, N+1):
    tmp = list(map(str, str(i)))
    check_list.extend(tmp)

print(check_list.count(str(M)))