# def solve(a):
#     return sum(a)

# import sys
# S = sys.stdin.readline().rstrip()
# bomb = sys.stdin.readline().rstrip()

# stack = []
# ex = len(bomb)

# for i in range(len(S)):
#     stack.append(S[i])
#     if ''.join(stack[-ex:]) == bomb:
#         for _ in range(ex):
#             stack.pop()

# if stack:
#     print(''.join(stack))
# else:
#     print('FRULA')

# import sys   시간초과

# S = sys.stdin.readline().rstrip()
# ex = sys.stdin.readline().rstrip()

# while ex in S:
#     S = S.replace(ex, '')

# if S:
#     print(S)
# else:
#     print('FRULA')
    
import sys

S = sys.stdin.readline().rstrip()
ex = sys.stdin.readline().rstrip()

stack = []
ex_len = len(ex)

for i in range(len(S)):
    stack.append(S[i])
    if ''.join(stack[-ex_len:]) == ex:
        for _ in range(ex_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')