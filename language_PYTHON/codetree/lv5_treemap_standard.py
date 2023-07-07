from sortedcontainers import SortedDict
import sys
si = sys.stdin.readline
sd = SortedDict()

N = int(si())

for i in range(N):
    cmd_list = list(map(str, si().strip().split()))
    if "add" in cmd_list:
        cmd, k, v = cmd_list
        sd[int(k)] = int(v)
    elif "remove" in cmd_list:
        cmd, k = cmd_list
        sd.pop(int(k))
    elif "find" in cmd_list:
        cmd, k = cmd_list
        if(int(k) not in sd.keys()):
            print("None")
        else:
            print(sd[int(k)])
    else:
        if len(sd) == 0:
            print("None")
        else:
            candidate = list(sd.values())
            print(*candidate)     