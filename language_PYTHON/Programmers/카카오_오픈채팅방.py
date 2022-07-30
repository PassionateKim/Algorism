# 2022-07-30
# 오픈채팅방

def solution(record):
    result = []
    id_nick_dict = dict()
    # 1.id: nick dict 저장
    for r in record:
        chars = r.split()
        
        # 데이터 길이가 3개일 때 (Enter, Change)
        if len(chars) == 3:
            id_nick_dict[chars[1]] = chars[2]
    # /1.id nick dict

    for r in record:
        cmd = r.split()[0] 
        id = r.split()[1]

        if cmd == "Enter":
            tmp = id_nick_dict[id] + "님이 들어왔습니다."
            result.append(tmp)
        elif cmd == "Leave":
            tmp = id_nick_dict[id] + "님이 나갔습니다."
            result.append(tmp)
        
        


    print(result)    
    return result
    

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 1. 나갈 때도 닉네임이 변경되는지 등 논리적인 부분을 명확히 하고 코드를 설계하자.
# 2. 이미 for 문을 돌면서 값을 활용할 수 있으면 굳이 dict를 추가할 필요는 없다.