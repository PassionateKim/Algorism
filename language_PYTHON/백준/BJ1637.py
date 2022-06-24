import sys
 
def check(x):
    global total
 
    # n줄에 주어진 구간에서 x보다 작거나 같은 수의 개수 구하기 - 누적합
    total = 0
    for i in li:
        # 계산하기 쉽게
        a, b, c = i[0], i[1], i[2]
        check = min(b, x)
        if check < a:
            total += 0
        else:
            total += ((check - a) // c) + 1
    return total
 
n = int(sys.stdin.readline().strip())
li = []
for i in range(n):
    a, c, b = map(int, sys.stdin.readline().strip().split())
    li.append([a, c, b])
 
s = 1
e = 10
 
# 이진 탐색
ans = -1
while s <= e:
    mid = (s + e) // 2
 
    if check(mid) % 2:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
 
if ans == -1:
    print("NOTHING")
else:
    print(ans, check(ans) - check(ans - 1))