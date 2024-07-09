from sys import stdin
from collections import deque
input = stdin.readline

dq = deque([])
result = []


for _ in range(int(input())):
    tmp = input().split()

    if tmp[0] == 'push_front':
        dq.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        dq.append(tmp[1])
    elif tmp[0] == 'pop_front':
        result.append(-1 if len(dq) == 0 else dq.popleft())
    elif tmp[0] == 'pop_back':
        result.append(-1 if len(dq) == 0 else dq.pop())
    elif tmp[0] == 'size':
        result.append(len(dq))
    elif tmp[0] == 'empty':
        result.append(1 if len(dq) == 0 else 0)
    elif tmp[0] == 'front':
        result.append(-1 if len(dq) == 0 else dq[0])
    else:
        result.append(-1 if len(dq) == 0 else dq[-1])
print(*result, sep='\n')
