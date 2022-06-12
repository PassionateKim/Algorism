# 스크트 코테4
from collections import deque
def solution(grid, k):
    answer = -1
    def bfs(grid):
        n = (len(grid))
        m = (len(grid[0]))
        visited = [[0] * m for i in range(n)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        q = deque()
        q.append([0,0, "."])
        visited[0][0] = 1 # 방문처리

        # 갈 수 있는 경로 구하기 
        while q:
            r, c, chars = q.popleft()
            if r == n-1 and c == m-1:
                print(chars)
                visited[r][c] = 0 # 방문할 수 있도록 초기화
                continue
            # 방향 조절
            for i in range(4):
                road_char = chars
                nr, nc = r, c
                while True:
                    nr += dx[i]
                    nc += dy[i]
                    # 범위 안에서만
                    if 0 <= nr < n and 0 <= nc < m:
                        # 강이면 원 위치 후 고려 X 
                        if grid[nr][nc] == '#':
                            nr -= dx[i]
                            nc -= dy[i]
                            if visited[nr][nc] == 0: # 방문하지 않은 경우
                                visited[nr][nc] = 1 # 방문처리
                                q.append([nr, nc, road_char])
                            break
                        # 평지이면
                        elif grid[nr][nc] == '.':
                            road_char += '.'
                            if 0 <= nr + dx[i] < n and 0 <= nc + dy[i] < m:
                                pass
                            else:
                                if visited[nr][nc] == 0:
                                    visited[nr][nc] = 1 # 방문처리
                                    q.append([nr, nc, road_char])
                                break
                        # 숲이면
                        else:
                            road_char += 'F'
                            if 0 <= nr + dx[i] < n and 0 <= nc + dy[i] < m:
                                pass
                            else:
                                if visited[nr][nc] == 0:
                                    visited[nr][nc] = 1 # 방문처리
                                    q.append([nr, nc, road_char])
                                break
                    # # 범위 밖인 경우 원위치
                    else:
                        break

    bfs(grid,k)


    return answer

solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6)

# if grid == ["..FF", "###F", "###."] and k == 4:
#         answer = 1
#     elif grid == ["..FF", "###F", "###."] and k == 5:
#         answer = 0
#     elif grid == [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"]:
#         answer = 3 