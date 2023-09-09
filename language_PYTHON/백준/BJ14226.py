# 복습 횟수:0, 02:00:00, 복습필요X
import sys
from collections import deque

si = sys.stdin.readline 
N = int(si())


def bfs():
    q = deque()
    visited1 = [[0 for _ in range(1000 + 1)] for _ in range(1000 + 1)]
    visited2 = [[0 for _ in range(1000 + 1)] for _ in range(1000 + 1)]
    visited3 = [[0 for _ in range(1000 + 1)] for _ in range(1000 + 1)]
    # 클립보드 개수, 현재 개수, 시간

    q.append([0, 1, 0])
    while q:
        clipboard_num, current_num, time = q.popleft()
        if current_num == N:
            print(time)
            break

        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        
        if visited1[clipboard_num][current_num] == 0:
            q.append([current_num, current_num, time + 1])
            visited1[clipboard_num][current_num] = 1

        # 클립보드에 있는 모든 이모티콘을 화면에 붙여 넣기 한다.
        # if clipboard_num >= 1 and visited[current_num + clipboard_num] == 0:
        if 0 <= current_num + clipboard_num <= 1000 and visited2[clipboard_num][current_num + clipboard_num] == 0:
            q.append([clipboard_num, current_num + clipboard_num, time + 1])
            visited2[clipboard_num][current_num + clipboard_num] = 1

        # 화면에 있는 이모티콘 중 하나를 삭제한다.
        # if visited[current_num - 1] == 0:
        if 0 <= current_num - 1 <= 1000 and visited3[clipboard_num][current_num - 1] == 0:
            q.append([clipboard_num, current_num - 1, time + 1])
            visited3[clipboard_num][current_num - 1] = 1
c
    return

bfs()