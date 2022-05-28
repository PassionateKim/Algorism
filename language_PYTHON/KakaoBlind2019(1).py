# 오픈채팅방
from collections import defaultdict, deque

def solution(record):
    answer = []
    nickName_dict = dict() # id: nickName
    
    for info in record:
        if info.split()[0] in "Enter&&Change":
            id, nick_name = info.split()[1], info.split()[2]
            nickName_dict[id] = nick_name
    
    for info in record:
        command, id = info.split()[0], info.split()[1]
        if command == "Enter":
            answer.append(nickName_dict[id]+"님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(nickName_dict[id]+"님이 나갔습니다.")
        
    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 1. 나갈 때도 닉네임이 변경되는지 등 논리적인 부분을 명확히 하고 코드를 설계하자.
# 2. 이미 for 문을 돌면서 값을 활용할 수 있으면 굳이 dict를 추가할 필요는 없다.