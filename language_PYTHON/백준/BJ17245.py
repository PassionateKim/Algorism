# 서버실
# 복습 횟수:0, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
room_list = []

for i in range(N):
    room = list(map(int, si().split()))
    room_list.extend(room)

room_list.sort()

computer = sum(room_list)
if (computer % 2) == 0:
    target = computer // 2 
else:
    target = computer // 2 + 1

answer = 0
def binary(start, end, target):
    global answer
    while start <= end:
        mid = (start + end) // 2
        sumi = 0
        for room in room_list:
            if room <= mid:
                sumi += room
            else:
                sumi += mid
        
        if sumi >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1  

    return

binary(0, max(room_list), target)
print(answer)