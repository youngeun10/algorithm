# Bronze 2
from sys import stdin
input = stdin.readline

stick = [int(input().rstrip()) for _ in range(int(input().rstrip()))]
n = stick.pop()
cnt = 1

while len(stick) > 0:
    tmp = stick.pop()
    if tmp > n:
        n = tmp
        cnt += 1
print(cnt)