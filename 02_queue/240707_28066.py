import sys
input = sys.stdin.readline
import collections

n, k = map(int, input().split())
arr = collections.deque([i for i in range(1, n+1)])

while len(arr) > k:
    arr.append(arr.popleft())
    for _ in range(k-1):
        arr.popleft()

print(arr.popleft())