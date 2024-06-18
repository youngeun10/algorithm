# Silver 4
from sys import stdin
input = stdin.readline
twins = {'(': ')', '[': ']'}

while True:
    tmp = input().rstrip()
    if tmp == '.':
        break
    stack = []
    sign = 'yes'
    for c in tmp:
        if c in ['(', '[']:
            stack.append(c)
        elif c in [')', ']']:
            if len(stack) == 0 or twins[stack[-1]] != c:
                sign = 'no'
                break
            elif twins[stack[-1]] == c:
                stack.pop()
    if len(stack) > 0: print('no')
    else: print(sign)

