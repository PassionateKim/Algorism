# 오픈채팅방
from collections import defaultdict, deque

def solution(record):
    answer = []
    command_dict = defaultdict(deque) # id: command
    nickName_dict = dict() # id: nickName
    # record 순서대로 체크
    for i in record:
        command = i.split()[0]
        if command == "Leave":
            id = i.split()[1]
            command_dict[id].append(command)
            # nickName_dict[id] = nickName
        else:
            id, nickName = i.split()[1], i.split()[2]
            command_dict[id].append(command)
            nickName_dict[id] = nickName
        
        
    print(command_dict)
    print(nickName_dict)
    for i in record:
        id = i.split()[1]
        if command_dict[id][0] == "Enter":
            answer.append(str(nickName_dict[id]) + "님이 들어왔습니다.")
        elif command_dict[id][0] == "Leave":
            answer.append(str(nickName_dict[id]) + "님이 나갔습니다.")        
        command_dict[id].popleft() 
    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])