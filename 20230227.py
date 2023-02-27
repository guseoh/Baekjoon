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


# while(True):
#     stack = []
#     a = input()
    
#     if a == '.':
#         break
    
#     for i in a: # 괄호 분류
#         if i =='[' or i == '(':
#             stack.append(i)
#         elif i == ']':
#             if len(stack) != 0 and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 stack.append(']')
#                 break
#         elif i == ')':
#             if len(stack) != 0 and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(')')
#                 break
            
#     if len(stack) == 0:
#         print('yes')
#     else: 
#         print('no')

# import math

# for _ in range(int(input())):
#     a, *arr = map(int, input().split())
#     total = 0
#     for j in range(a):
#         for k in range(j+1, a):
#             total += math.gcd(arr[j], arr[k])
#     print(total)

