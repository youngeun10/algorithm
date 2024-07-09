import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [str(i) for i in range(1, n+1)]
result = []
idx = 0
while arr:
    idx = (idx + (k-1)) % len(arr)
    result.append(arr[idx])
    arr.remove(arr[idx])

print("<%s>" %', '.join(result))