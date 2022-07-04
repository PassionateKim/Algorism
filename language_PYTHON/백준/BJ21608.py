# 상어 초등학교
import sys
from collections import defaultdict, deque
si = sys.stdin.readline

N = int(si())
graph = [[0 for _ in range(N)] for __ in range(N)]
student_dict = defaultdict(set)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 값 넣기
for i in range(N*N):
    a, *b = map(int, si().split())
    student_dict[a] = set(b)


def getFirstCandidate(like_list):
    arr = []
    maxi = -int(1e7)
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0: # 비어있는 칸중에서
                cnt = 0
                # 상하좌우
                for idx in range(4):
                    nx, ny = i + dx[idx], j + dy[idx]
                    
                    if not (0<=nx<N and 0<=ny<N): continue # 범위 밖X

                    if graph[nx][ny] in like_list: # 좋아하는 학생이 인접한 경우 O(1)
                        cnt += 1
                if maxi < cnt:
                    arr.clear()
                    arr.append((i, j))
                    maxi = cnt

                elif maxi == cnt:
                    arr.append((i, j))
    return arr

def getSecondCandidate(arr):
    tmp = []
    maxi = -int(1e7)
    for ar in arr:
        x, y = ar[0], ar[1] # 2, 2
        cnt = 0
        # 상하좌우
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0<=nx<N and 0<=ny<N): continue # 범위 밖X
            
            if graph[nx][ny] == 0: # 비어있는 칸인 경우
                cnt += 1

        if maxi < cnt:
            tmp.clear()
            tmp.append((x, y))
            maxi = cnt

        elif maxi == cnt:
            tmp.append((x, y))
    
    return tmp

for item in student_dict:
    student = item
    like_list = student_dict[student]
    
    # 1단계
    arr = getFirstCandidate(like_list)
    
    # 2단계
    arr2 = getSecondCandidate(arr)

    # 3단계
    arr2.sort(key=lambda x: (x[0], x[1])) # 행 -> 열 정렬
    graph[arr2[0][0]][arr2[0][1]] = student


answer = 0
for i in range(N):
    for j in range(N):
        tmp_list = student_dict[graph[i][j]] # 좋아하는 학생 list
        tmp = 0
        for idx in range(4): # 상하좌우
            nx, ny = i + dx[idx], j + dy[idx] 
            if not (0<=nx<N and 0<=ny<N): continue # 범위 아웃

            if graph[nx][ny] in tmp_list:
                tmp += 1 # 좋아하는 학생의 수 증가
        
        if tmp == 0:
            answer += 0
        elif tmp == 1:
            answer += 1
        elif tmp == 2:
            answer += 10
        elif tmp == 3:
            answer += 100
        elif tmp == 4:
            answer += 1000

print(answer)

