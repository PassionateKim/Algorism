# 복습 횟수:0, 01:00:00, 복습필요:***
from collections import deque
def solution(picks, minerals):
    answer = 0
    mineral_list = []
    tool_num = sum(picks)
    minerals = minerals[:5*tool_num]

    tmp = []
    for idx, mineral in enumerate(minerals):
        tmp.append(mineral)
        if idx % 5 == 4:
            mineral_list.append(tmp)
            tmp = []
        else:
            pass
    
    if len(tmp) != 0:
        mineral_list.append(tmp)
    
    indexed_list = []
    for mineral in mineral_list:
        dia = 0
        iron = 0
        stone = 0
        for m in mineral:
            if m == "diamond":
                dia += 1
            elif m == "iron":
                iron += 1
            else:
                stone += 1
        indexed_list.append([dia, iron, stone])

    indexed_list.sort(key=lambda x:[-x[0], -x[1], -x[2]])

    tool_list = deque()
    for idx, pick in enumerate(picks):
        if idx == 0:
            for i in range(pick):
                tool_list.append("dia")
        elif idx == 1:
            for i in range(pick):
                tool_list.append("iron")
        else:
            for i in range(pick):
                tool_list.append("stone")

    
    for dia_num, iron_num, stone_num in indexed_list:

        tool = tool_list.popleft()
        if tool == "dia":
            answer  = answer + (dia_num + iron_num + stone_num)
        elif tool == "iron":
            answer = answer + (dia_num * 5 + iron_num + stone_num)
        else:
            answer = answer + (dia_num * 25 + iron_num * 5 + stone_num)

    return answer

print(solution([0, 0, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))