import sys
si = sys.stdin.readline

myDict = dict()
N = int(si())

for i in range(N):
    commands = list(map(str, si().split()))
    if len(commands) ==  3:
        cmd, k, v = commands
        myDict[k] = v
    else:
        cmd, k = commands
        if(cmd == 'find'):
            if (k in myDict.keys()):
                print(myDict[k])
            else:
                print("None")
        else: # remove
            myDict.pop(k)
