# 로또
import sys
si = sys.stdin.readline 

def dfs(depth, index, candidate_list: list):
    if depth == 6:
        print(*candidate_list)
        return


    for i in range(index, len(number_list)):
        target = number_list[i]

        candidate_list.append(target)
        dfs(depth + 1, i+1, candidate_list)
        candidate_list.pop()

    return

while True:
    input_list = list(map(int, si().split()))

    if len(input_list) == 1 and input_list[0] == 0:
        break

    num = input_list[0]
    
    number_list = input_list[1:]

    dfs(0, 0, [])
    print()