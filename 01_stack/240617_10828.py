# silver 10828
from sys import stdin
input = stdin.readline

from collections import deque
st = deque([])

inputArr = [input().split() for _ in range(int(input()))]

for i in range(len(inputArr)):
    if inputArr[i][0] == 'push':
        st.append(inputArr[i][1])
    elif inputArr[i][0] == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
    elif inputArr[i][0] == 'size':
        print(len(st))
    elif inputArr[i][0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())




