# galho = input()
# stack = []
# answer = 0

# for i in range(len(galho)):
#     if galho[i] == '(':
#         stack.append(galho[i])
#     else:
#         if galho[i-1] == '(':
#             stack.pop()
#             answer += len(stack)
#         else:
#             stack.pop()
#             answer += 1
# print(answer)

# n, k = map(int, input().split())
# number = list(input())

# answer = []
# cnt = k
# for num in number:
#     while answer and cnt>0 and answer[-1] <num:
#         del answer[-1]
#         cnt -= 1
#     answer.append(num)
# print("".join(answer[:n-k]))

# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# queue = deque([])

# for i in range(n):
#     command = input().split()
#     if command[0] == 'push': # push 삽입
#         queue.append(command[1])
#     elif command[0] == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             print(queue.popleft()) # 큐의 전단을 출력하고 삭제
#     elif command[0] == 'size':
#         print(len(queue))
#     elif command[0] == 'empty':
#         if not queue:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'front':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[0])
#     elif command[0] == 'back':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[-1])

test = int(input())
for i in range(test):
    map = {}
    answer = 1
    n = int(input())
    for j in range(n):
        a,b = input().split()
        if not b in map:
            map[b] = 1
        else: # 의상의 종류가 존재하면 키 값 1 증가
            map[b] += 1
    for k in map.keys():
        answer *= (map[k]+1)
    print(answer - 1)