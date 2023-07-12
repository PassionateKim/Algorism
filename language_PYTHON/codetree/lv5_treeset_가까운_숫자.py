# 복습횟수:0, 00:30:00, 복습필요:*
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline 

# 복습 횟수:0, 00:30:00, 복습필요:*
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline
N = int(si())

dot_list = list(map(int, si().split()))
s = SortedSet()

s.add(0)
ans = 1e11
for dot in dot_list:
    # 가장 근처에 있는 오른쪽 점 찾기
    idx = s.bisect_right(dot)
    if (idx != len(s)):
        ans = min(ans, s[idx] - dot) 


    # 가장 근처에 있는 왼쪽 점 찾기
    idx -= 1
    ans = min(ans, dot - s[idx])
    s.add(dot)
    print(ans)
