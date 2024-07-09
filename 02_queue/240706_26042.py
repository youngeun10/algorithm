"""
    * 입력
    n: 줄
    1 a: a번 학생이 대기 줄에 섬
    2: 맨 앞 친구가 밥 먹고 나감

    * 출력
    최대로 기다린 학생 수,
    맨 뒤에 있는 학생 번호 (만약에 같은 학생 수 가 있었으면 맨 뒤 작은 번호)
"""
import sys
input = sys.stdin.readline

import collections
dq = collections.deque([])
maxLen = 0
lastNum = 0

for _ in range(int(input())):
    tmp = input().rstrip()

    if tmp[0] == '1':
        n, a = tmp.split()
        dq.append(int(a))

        if maxLen < len(dq):
            maxLen = len(dq)
            lastNum = dq[-1]
        elif maxLen == len(dq):
            if lastNum > dq[-1]:
                lastNum = dq[-1]
    else:
        dq.popleft()
print(maxLen, lastNum)
