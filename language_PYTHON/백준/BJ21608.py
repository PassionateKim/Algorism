# 상어 초등학교
# 복습 횟수:2, 01:00:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
student_list = []
student_dict = dict()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N*N):
    student = list(map(int, si().split()))
    student_list.append(student)
    student_dict[student[0]] = student[1:]
graph = [[0 for _ in range(N)] for __ in range(N)]

# 탐색 시직
for student in student_list:
    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    target = student[0]
    like_student = set(student[1:]) # 시간복잡도를 줄이기 위해  해시 사용

    like_list = []
    for x in range(N):
        for y in range(N):
            if graph[x][y] != 0: continue
            cnt = 0
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if not (0 <= nx < N and 0 <= ny <N): continue
                if graph[nx][ny] in like_student:
                    cnt += 1
            like_list.append([x, y, cnt])
    max_like_index = [] # 가장 max 찾기
    maxi = 0
    for i in range(len(like_list)):
        maxi = max(maxi, like_list[i][2])

    for i in range(len(like_list)):
        if like_list[i][2] == maxi:
            max_like_index.append([like_list[i][0], like_list[i][1], like_list[i][2]])

    if len(max_like_index) == 1:
        x = max_like_index[0][0]
        y = max_like_index[0][1]
        graph[x][y] = target
        continue
    else: # 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        empty_list = []
        for i in range(len(max_like_index)):
            x = max_like_index[i][0]
            y = max_like_index[i][1]
            cnt = 0
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if not( 0 <= nx < N and 0 <= ny < N): continue
                if graph[nx][ny] == 0: #비어있다면
                    cnt += 1
            empty_list.append([x, y, cnt])
        maxi = 0
        for i in range(len(empty_list)):
            maxi = max(maxi, empty_list[i][2])
        tmp = []
        for i in range(len(empty_list)):
            if empty_list[i][2] == maxi:
                tmp.append([empty_list[i][0], empty_list[i][1]])
        
        if len(tmp) == 1:
            graph[tmp[0][0]][tmp[0][1]] = target
        else: # 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
            tmp.sort(key=lambda x: (x[0], x[1]))
            graph[tmp[0][0]][tmp[0][1]] = target

# 만족도의 총합 구하기
answer = 0
for x in range(N):
    for y in range(N):
        target = graph[x][y]
        value = student_dict[target]
        cnt = 0
        for idx in range(4):
            nx,  ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < N):continue
            if graph[nx][ny] in value:
                cnt += 1
        
        if cnt == 0:
            answer += 0
        elif cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        else:
            answer += 1000
print(answer)
    
