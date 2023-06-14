# 컨베이어 벨트 위의 로봇
# 복습 횟수:0, 01:15:00, 복습필요O
import sys
si = sys.stdin.readline 
N, K = map(int, si().split())
container_list = list(map(int, si().split()))
robot_list = [0 for i in range(N)]

answer = 0

while True:
    answer += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    # 1-1 벨트 
    to_be_first = container_list[-1]
    
    for i in range(len(container_list)-2, -1, -1):
        container_list[i+1] = container_list[i] # 오른쪽으로 한칸 이동시킨다.
    container_list[0] = to_be_first

    # 1-2 로봇
    for i in range(len(robot_list)-2, -1, -1):
        if(robot_list[i] == 1):
            robot_list[i+1] = robot_list[i] # 오른쪽으로 한칸 이동시킨다.
            robot_list[i] = 0 
    robot_list[-1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    #    로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(len(robot_list)-2, -1, -1):
        if(robot_list[i] == 1 and robot_list[i+1] == 0): # 로봇이 존재하고
            if(container_list[i+1] >= 1): # 내구도가 1 이상일 때
                robot_list[i+1] = robot_list[i] # 로봇을 이동시키고
                robot_list[i] = 0
                container_list[i+1] -= 1 # 내구도를 1 줄인다.
    robot_list[-1] = 0 # 내릴 수 있으면 바로 내린다.


    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올린다.
    if(container_list[0] >= 1):
        robot_list[0] = 1 # 로봇을 올린다.
        container_list[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if(container_list.count(0) >= K):
        break

print(answer)