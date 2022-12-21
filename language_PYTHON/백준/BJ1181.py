import sys
si = sys.stdin.readline

N = int(si())

sss = set()

for i in range(N):
    tmp = si().rstrip()
    sss.add(tmp)

sss = list(sss)
sss.sort(key=lambda x: (len(x), x))

for i in sss:
    print(i)