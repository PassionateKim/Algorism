def solution(keymaps, targets):
    answer = []
    key_dict = dict()
    
    for keymap in keymaps:
        for idx in range(len(keymap)):
            if keymap[idx] in key_dict.keys():
                val = min(key_dict[keymap[idx]], idx)
                key_dict[keymap[idx]] = val 
            else:
                key_dict[keymap[idx]] = idx 
    
    for target in targets:
        tmp = 0
        flag = False
        for s in target:
            if s in key_dict.keys():
                tmp += (key_dict[s] + 1)
            else:
                flag = True
                break
        if flag:
            answer.append(-1)
        else:
            answer.append(tmp)

    return answer

solution(["ABACD", "BCEFD"], ["XABCD", "AABB"])