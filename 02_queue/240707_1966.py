import sys
input = sys.stdin.readline
import collections

for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = collections.deque(list(map(int, input().split())))
    arr = collections.deque([(i, idx) for idx, i in enumerate(arr)])

    cnt = 0
    while True:
        if arr[0][0] == max(arr, key=lambda x: x[0])[0]:
            cnt += 1
            if arr[0][1] == q:
                print(cnt)
                break
            else:
                arr.popleft()
        else:
            arr.append(arr.popleft())


