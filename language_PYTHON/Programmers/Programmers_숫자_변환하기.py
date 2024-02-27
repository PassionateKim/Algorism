from collections import deque

def solution(x, y, n):
    answer = -1  

    q = deque()
    q.append([x, 0]) # 숫자, 횟수
    visited = [0 for i in range(1000001)]

    while q:
        number, count = q.popleft()
        if number == y:
            answer = count
            break

        if 1 <= number + n <= 1000000 and visited[number + n] == 0:
            q.append([number + n, count + 1]) # q에 삽입
            visited[number + n] = 1 # 방문처리
        
        if 1 <= number * 2 <= 1000000 and visited[number * 2] == 0:
            q.append([number * 2, count + 1]) # q에 삽입
            visited[number * 2] = 1 # 방문처리

        if 1 <= number * 3 <= 1000000 and visited[number * 3] == 0:
            q.append([number * 3, count + 1]) # q에 삽입
            visited[number * 3] = 1 # 방문처리

    return answer

solution(10, 40, 30)