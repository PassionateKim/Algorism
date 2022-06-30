# 상어 초등학교
from collections import defaultdict
import sys
si = sys.stdin.readline

# 최대 N*3 가능 20 * 20 * 20 = 8000번 계산
N = int(si())
graph = [[0 for i in range(N)] for i in range(N)]
sum = 0
student_like = defaultdict(set) # 순서가 필요함

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N*N):
    student, *like = map(int, si().split())
    student_like[student] = like


def getFirstCandidate(like):
    like = set(like) # 집합으로 변경-> 해시로 O(1)
    arr = []
    maxi = -1e6
    for i in range(N):
        for j in range(N):
            flag = 0

            for idx in range(4): # 상하좌우 탐색
                nx, ny = i + dx[idx], j + dy[idx]
                if not (0<=nx<N and 0<=ny<N): continue # 범위 내에
                if graph[i][j] != 0: continue # 비어있는 칸 중에서

                if graph[nx][ny] in like:
                    flag += 1
            # 좋아하는 학생이 있는 칸 수를 비교
            if maxi < flag: # 크면 모두 초기화
                arr.clear() # 초기화
                maxi = flag
                arr.append((i,j))
            elif maxi == flag:
                arr.append((i,j))
    return arr

def getSecondCandidate(seti):
    arr = []
    maxi = -1e6
    for item in seti:
        flag = 0
        for idx in range(4):
            nx, ny = item[0] + dx[idx], item[1] + dy[idx]
            if not (0<=nx<N and 0<=ny<N): continue
                
            if graph[nx][ny] == 0: # 비어있는 칸
                flag += 1

        if maxi < flag:
            arr.clear() # 초기화
            maxi = flag
            arr.append((item[0],item[1]))
        elif maxi == flag:
            arr.append((item[0],item[1]))

    return arr    

for student in student_like: # 1단계
    arr = getFirstCandidate(student_like[student])
    
    # 2단계
    arr = getSecondCandidate(arr)
    
    # 3단계
    arr.sort(key = lambda x: (x[0], x[1]))
    graph[arr[0][0]][arr[0][1]] = student


# 만족도 구하기
answer = 0

for i in range(N):
    for j in range(N):
        
        tmp = 0
        key, value = graph[i][j] , student_like[graph[i][j]]
        for idx in range(4):
            nx, ny = i + dx[idx], j + dy[idx]
            if not (0<=nx<N and 0<=ny<N): continue
            if graph[nx][ny] in value:
                tmp += 1
        # 만족도 
        if tmp == 0 or tmp == 1:
            answer += 1
        elif tmp == 2:
            answer += 10
        elif tmp == 3:
            answer += 100
        else:
            answer += 1000
for i in graph:
    print(i)
print(answer)