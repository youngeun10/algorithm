import sys
input = sys.stdin.readline

n, p = map(int, input().split())
st = [[] for i in range(7)]
cnt = 0
for _ in range(n):
    l, p = map(int, input().rstrip().split())

    if len(st[l]) > 0 and st[l][-1] > p:
        while len(st[l]) > 0 and st[l][-1] > p:
            st[l].pop()
            cnt += 1
    if len(st[l]) == 0 or st[l][-1] < p:
        cnt += 1
        st[l].append(p)

print(cnt)