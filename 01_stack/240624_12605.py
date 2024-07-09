import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    arr = list(input().rstrip().split())
    arr.reverse()
    result.append(arr)

for i in range(n):
    print("Case #%d: %s" %((i+1), ' '.join(result[i])))
