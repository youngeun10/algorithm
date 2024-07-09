import sys
input = sys.stdin.readline

from collections import deque
q = deque(list([]))

for _ in range(int(input())):
    tmp = input().rstrip().split()

    if tmp[0] == 'push':
        q.append(tmp[1])
    elif tmp[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(q))
    elif tmp[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])