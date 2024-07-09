from sys import stdin
from collections import deque
input = stdin.readline

n, x = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
num = list(map(int, input().split()))

cnt = 0
for i in num:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
