import sys
si = sys.stdin.readline 
target_str = list(map(str, si().rstrip()))
should_change = target_str[1]
result_change = target_str[4]

new_target_str = []

for target_s in target_str:
    if target_s == should_change:
        new_target_str.append(result_change)
    else:
        new_target_str.append(target_s)

print("".join(new_target_str))