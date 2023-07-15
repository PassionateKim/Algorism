# 복습횟수:0, 01:00:00, 복습필요:***
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline
s = SortedSet()
N = int(si())

for i in range(N):
    P, L = map(int, si().split())

    s.add(tuple([L, P]))

M = int(si())
def removeProblem(level, pNumber):
    start = 0
    end = len(s) - 1

    while start <= end:
        mid = (start + end) // 2
        if s[mid][0] == level:
            if s[mid][1] == pNumber:
                s.remove(tuple([level, pNumber]))
                return
            if s[mid][1] > pNumber:
                end = mid - 1
            
            if s[mid][1] < pNumber:
                start = mid + 1

        if s[mid][0] > level:
            end = mid - 1
        
        if s[mid][0] < level:
            start = mid + 1

def printHardest():
    print(s[-1][1])

def printEasiest():
    print(s[0][1])

for i in range(M):
    cmd_list = list(map(str, si().rstrip().split()))
    # add
    if "ad" in cmd_list:
        cmd, P, L = cmd_list
        input = tuple([int(L), int(P)])
        s.add(input)
    elif "sv" in cmd_list:
        # 삭제하기 P 번호의 난이도 L 문제 삭제
        cmd, P, L = cmd_list
        removeProblem(int(L), int(P))

    elif "rc" in cmd_list:
        cmd, key = cmd_list
        key = int(key)
        # 가장 난이도 높은 문제 번호 - 여러개면 문제 번호 큰 것으로 출력 1
        if key == 1:
            printHardest()
        # 가장 난이도 낮은 문제 번호 - 여러개면 문제 번호 낮은 것으로 출력 -1
        else:
            printEasiest()