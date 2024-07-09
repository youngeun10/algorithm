import sys
input = sys.stdin.readline

import collections
chk = 0

for _ in range(int(input())):
    s = input().rstrip()
    d = collections.deque(list([]))
    for i in s:
        if i == '(':
            d.append(i)
        else:
            if len(d) > 0:
                p = d.pop()
                if p != ')':
                    chk = 1
            else:
                chk = 1

    if len(d) == 0:
        print("YES")
    else:
        print("NO")

