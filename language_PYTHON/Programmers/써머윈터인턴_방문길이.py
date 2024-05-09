# 2022-09-20
# 2024-05-09
# 방문 길이
def solution(dirs):
    answer = list()
    
    location = [0, 0]
    for dir in dirs:
        if dir == 'U':
            if location[1] + 1 > 5: continue
            answer.append(tuple([location[0], location[1], location[0], location[1] + 1]))
            location[1] += 1
        if dir == 'D':
            if location[1] - 1 < -5: continue
            answer.append(tuple([location[0], location[1] - 1, location[0], location[1]]))
            location[1] -= 1
        if dir == 'L':
            if location[0] - 1 < -5: continue
            answer.append(tuple([location[0] - 1, location[1], location[0], location[1]]))
            location[0] -= 1
        if dir == 'R':
            if location[0] + 1 > 5: continue
            answer.append(tuple([location[0], location[1], location[0] + 1, location[1]]))
            location[0] += 1
            
    return len(set(answer)) 
