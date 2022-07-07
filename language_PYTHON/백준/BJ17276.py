# 배열 돌리기
import sys
si = sys.stdin.readline

def getHang():
    x, y = N//2, 0
    arr = []

    while y < N:
        arr.append(graph[x][y])
        y += 1

    return arr

def getJuDagak():
    x, y = 0, 0
    arr = []

    while x < N:
        arr.append(graph[x][y])
        x += 1
        y += 1

    return arr

def getYeol():
    x, y = 0, N//2
    arr = []


    while x < N:
        arr.append(graph[x][y])
        x += 1
    
    return arr

def getBuDagak():
    x, y = N-1, 0
    arr = []

    while x >= 0:
        arr.append(graph[x][y])
        x -= 1
        y += 1

    return arr    

T = int(si())
for i in range(T):
    N, angle = map(int, si().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, si().split())))
    # 2차원 배열에 대각선, 열, 행 저장하기
    arr = []

    hang = getHang()    
    juDagak = getJuDagak()
    yeol = getYeol()
    buDagak = getBuDagak()
    
    # 값 넣기
    arr.append(hang)
    arr.append(juDagak)
    arr.append(yeol)
    arr.append(buDagak)
    
    # 행 주 열 부
    
    # 45, 90, 135인 경우 < 180 인 경우
    if angle == 45: # 45도인 경우 
        arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], list(reversed(arr[2]))
    
    elif angle == 90: # 90도인 경우
        arr[0], arr[1], arr[2], arr[3] = list(reversed(arr[2])), arr[3], arr[0], list(reversed(arr[1]))
    
    elif angle == 135: # 135도 인 경우
        arr[0], arr[1], arr[2], arr[3] = list(reversed(arr[1])), list(reversed(arr[2])), arr[3], list(reversed(arr[0]))
    
    elif angle == 180: # 180도 인 경우
        arr[0].reverse()
        arr[1].reverse()
        arr[2].reverse()
        arr[3].reverse()

    elif angle == 225: # 225도 인 경우
        # for i in arr:
        #     print(i)
        # print("---")
        arr[0], arr[1], arr[2], arr[3] = list(reversed(arr[3])), list(reversed(arr[0])), list(reversed(arr[1])), arr[2]

    elif angle == 270:
        arr[0], arr[1], arr[2], arr[3] = arr[2], list(reversed(arr[3])), list(reversed(arr[0])), arr[1]
    
    elif angle == 315:
        arr[0], arr[1], arr[2], arr[3] = arr[1], arr[2], list(reversed(arr[3])), arr[0]

    elif angle == 360:
        pass
    
    # 마이너스
    if angle == -45: # 45도인 경우 
        arr[0], arr[1], arr[2], arr[3] = arr[1], arr[2], list(reversed(arr[3])), arr[0]
    
    elif angle == -90: # 90도인 경우
        arr[0], arr[1], arr[2], arr[3] = arr[2], list(reversed(arr[3])), list(reversed(arr[0])), arr[1]
    
    elif angle == -135: # 135도 인 경우
        arr[0], arr[1], arr[2], arr[3] = list(reversed(arr[3])), list(reversed(arr[0])), list(reversed(arr[1])), arr[2]
    
    elif angle == -180: # 180도 인 경우
        arr[0].reverse()
        arr[1].reverse()
        arr[2].reverse()
        arr[3].reverse()
    
    elif angle == -225: # 225도 인 경우
        arr[0], arr[1], arr[2], arr[3] = list(reversed(arr[1])), list(reversed(arr[2])), arr[3], list(reversed(arr[0]))

    elif angle == -270:
        arr[0], arr[1], arr[2], arr[3] = list(reversed(arr[2])), arr[3], arr[0], list(reversed(arr[1]))
    
    elif angle == -315:
        arr[0], arr[1], arr[2], arr[3] = arr[3], arr[0], arr[1], list(reversed(arr[2]))
    elif angle == -360:
        pass

    
    # 행
    graph[N//2] = arr[0]
    
    # 주대각
    x, y = 0, 0
    for i in arr[1]:
        graph[x][y] = i
        x += 1
        y += 1
    # 열
    x, y = 0, N//2
    for i in arr[2]:
        graph[x][y] = i
        x += 1 
    x, y = N-1, 0
    for i in arr[3]:
        graph[x][y] = i
        x -= 1
        y += 1
    
    for i in graph:
        print(*i)