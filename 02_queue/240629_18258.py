import sys
input = sys.stdin.readline
q, result = [], []
s, e = 0, 0
# 연산
# push pop size empty front back
for _ in range(int(input())):
    tmp = input().rstrip().split()
    if tmp[0] == 'push':
        q.append(int(tmp[1]))
        e += 1
    elif tmp[0] == 'pop':
        if e == s:
            result.append(-1)
        else:
            result.append(q[s])
            s += 1
    elif tmp[0] == 'size':
        result.append(e-s)
    elif tmp[0] == 'empty':
        result.append(1 if e == s else 0)
    elif tmp[0] == 'front':
        result.append(-1 if e == s else q[s])
    else:
        result.append(-1 if e == s else q[e-1])

print(*result, sep='\n')
