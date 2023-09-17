import sys
si = sys.stdin.readline 

L, C = map(int, si().split())
alphabet_list = list(map(str, si().split()))
alphabet_list.sort()

mo_um = set(['a','e','i','o','u'])

def dfs(depth, index, candidate_list: list):

    if depth == L:
        za_um_count = 0
        mo_um_count = 0

        for string_ in candidate_list:
            if string_ in mo_um:
                mo_um_count += 1
            else:
                za_um_count += 1

        if mo_um_count >= 1 and za_um_count >= 2:
            print("".join(candidate_list))
        return
    
    for i in range(index, len(alphabet_list)):
        val = alphabet_list[i]
        candidate_list.append(val)
        dfs(depth + 1, i + 1, candidate_list)
        candidate_list.pop()

    return


dfs(0, 0, [])