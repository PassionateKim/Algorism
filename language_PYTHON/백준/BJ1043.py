import sys
si = sys.stdin.readline 

N, M = map(int, si().split())
know_list = list(map(int, si().split()))
know_list = know_list[1:]
know_set = set(know_list)

party_list = []

for i in range(M):
    tmp = list(map(int, si().split()))
    tmp = tmp[1:]
    party_list.append(tmp)


answer = 0
def dfs(depth, count, hear_check: list):
    global answer

    if depth == M:
        answer = max(answer, count)
        return
    
    current_party = party_list[depth]
    is_know_here = False
    # 진실을 아는 사람이 있는 경우
    for current_person in current_party:
        if current_person in know_set:
            is_know_here = True
    
    # 2 과장, 1 진실
    if is_know_here:
        change_memory = [0 for i in range(N + 1)]
        is_lier = False

        for current_person in current_party:
            if hear_check[current_person] == 0: 
                hear_check[current_person] = 1
                change_memory[current_person] = 1 

            elif hear_check[current_person] == 1:
                pass

            else: # 과장을 했던 경우 안되는  케이스이므로
                is_lier = True

        if not is_lier:        
            dfs(depth + 1, count, hear_check)

        for i in range(len(change_memory)):
            if change_memory[i] == 1:
                hear_check[i] = 0 # 변환했던 index는 초기화

    else: # 진실을 아는 사람이 없는 경우 
        # 과장을 하는 경우
        change_memory = [0 for i in range(N + 1)]
        is_lier = False

        for current_person in current_party:
            if hear_check[current_person] == 0:
                hear_check[current_person] = 2 # 과장
                change_memory[current_person] = 1
            
            elif hear_check[current_person] == 1: # 진실을 말했던 경우는 안되는 케이스이므로
                is_lier = True
            else:
                pass
        
        if not is_lier:
            dfs(depth + 1, count + 1, hear_check)

        for i in range(len(change_memory)):
            if change_memory[i] == 1:
                hear_check[i] = 0 # 변환했던 index는 초기화

        # 과장을 안하는 경우
        change_memory = [0 for i in range(N + 1)]
        is_lier = False

        for current_person in current_party:
            if hear_check[current_person] == 0: 
                hear_check[current_person] = 1
                change_memory[current_person] = 1 

            elif hear_check[current_person] == 1:
                pass

            else: # 과장을 했던 경우 안되는  케이스이므로
                is_lier = True

        if not is_lier:        
            dfs(depth + 1, count, hear_check)

        for i in range(len(change_memory)):
            if change_memory[i] == 1:
                hear_check[i] = 0 # 변환했던 index는 초기화

    return

hear_check = [0 for i in range(N + 1)]
dfs(0, 0, hear_check)

print(answer)