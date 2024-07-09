from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
arr = deque([str(i) for i in range(1, n+1)])
cnt, result = 1, []
while len(arr) > 0:
    if cnt == k:
        result.append(arr.popleft())
        cnt = 0
    else:
        tmp = arr.popleft()
        arr.append(tmp)
    cnt += 1
print("<%s>" %', '.join(result))
