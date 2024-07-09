import sys
input = sys.stdin.readline

n = int(input())
f = list(map(int, input().rstrip().split()))
chk = list(map(int, input().rstrip().split()))

result = 0
for i in range(n):
    if not chk[i]:
        result += f[i]
print(sum(f))
print(result)