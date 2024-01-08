import sys
from collections import defaultdict
from collections import deque

si = sys.stdin.readline 

# 뱀의 위치 정보를 기억하는 배열
# graph
# 뱀의 방향 정보

time = 0
N = int(si())
K = int(si())

location_change_dict = defaultdict(str)
graph = [[0 for i in range(N)] for i in range(N)]

for i in range(K):
    x, y = list(map(int, si().split()))
    
    graph[x-1][y-1] = 1 # 사과의 위치 저장

L = int(si())
for i in range(L):
    key, value = list(map(str, si().split()))

    location_change_dict[key] = value
    
dir = "right"
q = deque()
q.append([0, 0])

snake = [[0 for i in range(N)] for i in range(N)]
snake[0][0] = 1
def locate_head(dir):

    if dir == "right":
        x, y = q[-1]
        nx, ny = x, y + 1
        
        if not (0 <= nx < N and 0 <= ny < N): 
            return False
        
        if [nx, ny] in q:
            return False
        
        q.append([nx, ny])
        snake[nx][ny] = 1

        if (graph[nx][ny] == 0): # 사과가 없다면 
            tail_x, tail_y = q.popleft()
            snake[tail_x][tail_y] = 0

        else:
            graph[nx][ny] = 0
        
        
    elif (dir == "left"):
        x, y = q[-1]
        nx, ny = x, y - 1
        if not (0 <= nx < N and 0 <= ny < N): 
            return False
        
        if [nx, ny] in q:
            return False
        
        q.append([nx, ny])
        snake[nx][ny] = 1

        if (graph[nx][ny] == 0): # 사과가 없다면 
            tail_x, tail_y = q.popleft()
            snake[tail_x][tail_y] = 0

        else:
            graph[nx][ny] = 0

    elif (dir == "top"):
        x, y = q[-1]
        nx, ny = x - 1, y 
        
        if not (0 <= nx < N and 0 <= ny < N): 
            return False
        
        if [nx, ny] in q:
            return False
        
        q.append([nx, ny])
        snake[nx][ny] = 1

        if (graph[nx][ny] == 0): # 사과가 없다면 
            tail_x, tail_y = q.popleft()
            snake[tail_x][tail_y] = 0

        else:
            graph[nx][ny] = 0

    else:
        x, y = q[-1]
        nx, ny = x + 1, y 
        
        if not (0 <= nx < N and 0 <= ny < N): 
            return False
        if [nx, ny] in q:
            return False
        
        q.append([nx, ny])
        snake[nx][ny] = 1

        if (graph[nx][ny] == 0): # 사과가 없다면 
            tail_x, tail_y = q.popleft()
            snake[tail_x][tail_y] = 0

        else:
            graph[nx][ny] = 0

    return True

def get_converted_dir(val):

    if(dir == "right"):
        if(val == 'L'):
            return "top"
        else:
            return "down"
        
    if(dir == "left"):
        if(val == 'L'):
            return "down"
        else:
            return "top"

    if(dir == "top"):
        if( val == 'L'):
            return "left"
        else:
            return "right"

    if(dir == "down"):
        if ( val == 'L'):
            return "right"
        else:
            return "left"
# 0: 오, 1: 왼, 2: 상: 3: 하
while True:
    
    isNoError = locate_head(dir)
    time += 1
    if( str(time) in location_change_dict.keys()):
        val = location_change_dict[str(time)]
        dir = get_converted_dir(val) 

    if not isNoError:
        print(time)
        break