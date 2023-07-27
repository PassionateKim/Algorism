# 컨베이어 벨트 위의 로봇
# 복습 횟수:1, 01:00:00, 복습필요2
import sys
si = sys.stdin.readline 

N, K = map(int, si().split())
belt_list = list(map(int, si().split()))
robot_list = [0 for i in range(N)]

answer = 0

def belt_rotate(belt_list):
    tmp = []
    tmp.append(belt_list[-1])
    tmp = tmp + belt_list[:-1]
    
    return tmp[:]

def robot_rotate(robot_list):
    for i in range(len(robot_list) - 2, -1, -1):
        robot_list[i+1] = robot_list[i]
        robot_list[i] = 0

    robot_list[-1] = 0 # 마지막 위치는 그 즉시 내린다.

    return robot_list[:]

def robot_move(belt_list, robot_list):
    for i in range(len(robot_list) - 2, -1, -1):
        if robot_list[i] == 1: # 로봇이 있는 경우
            if robot_list[i+1] == 0 and belt_list[i+1]: # 앞에 로봇이 없고 앞 칸에 내구도가 1이상인 경우
                robot_list[i+1] = robot_list[i]
                robot_list[i] = 0
                belt_list[i+1] -= 1 # 내구도를 깎는다.
    
    robot_list[-1] = 0 # 마지막 위치는 즉시 내린다.

    return

def robot_upload(belt_list, robot_list):
    if belt_list[0]:
        robot_list[0] = 1
        belt_list[0] -= 1

    return
while True:
    # 탈출 조건
    if belt_list.count(0) >= K:
        print(answer)
        break

    answer += 1
    # 비지니스 로직
    # 회전 with Robot
    # 1. 벨트
    belt_list = belt_rotate(belt_list)

    robot_list = robot_rotate(robot_list)  

    # 2. 로봇
    # 이동
    robot_move(belt_list, robot_list)

    # 로봇 올리기
    robot_upload(belt_list, robot_list)