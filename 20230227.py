# import sys
# input = sys.stdin.readline

# stack = []

# for _ in range(int(input())):
#     a = []
#     a = list(input().split())
#     if a[0] == 'push':
#         stack.append(int(a[1]))
#     elif a[0] == 'top':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])
#     elif a[0] == 'size':
#         print(len(stack))
#     elif a[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else: print(0)
#     elif a[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())


# for i in range(int(input())):
#     stack = []
#     a = input()
#     for j in a:
#         if j == '(':
#             stack.append('(')
#         elif j == ')':
#             if stack:
#                 stack.pop()
#             else:
#                 print("NO")
#                 break
#     else:
#         if not stack:
#             print('YES')
#         else: print('NO')
    
while(True):
    stack = []
    a = input()
    
    if a == '.':
        print('.')
        break
    for i in a:
        if i == '(' or ')' or '[' or ']':
            stack.append(i)
        else: continue
    print(stack)