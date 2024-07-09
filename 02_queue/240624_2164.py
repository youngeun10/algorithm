import sys
input = sys.stdin.readline
import collections

arr = collections.deque([i for i in range(1, int(input())+1)])

while True:
    if len(arr) == 1:
        print(arr[0])
        break

    arr.popleft()
    arr.append(arr.popleft())


