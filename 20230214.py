# n = input().split()
# print(len(n))

# alphbet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# time = 0
# for i in range(len(a)):
#     for j in alphbet:
#         if a[i] in j:
#             time += alphbet.index(j) + 3
# print(time)

# n = int(input())
# title = 666
# cnt = 0
# while(True):
#     if "666" in str(title):
#         cnt += 1
#         if cnt == n:
#             print(title)
#             break
#     title += 1


# 완전 탐색
# n,m = map(int, input().split())
# board = []
# answer = []

# for _ in range(n):
#     board.append(input())

# for col in range(n - 7):
#     for row in range(m - 7):
#         w = 0 # White
#         b = 0 # Black
#         for i in range(col, col + 8):
#             for j in range(row, row + 8):
#                 if (i + j) % 2 == 0:
#                     if board[i][j] != 'W':
#                         w += 1
#                     if board[i][j] != 'B':
#                         b += 1
#                 else:
#                     if board[i][j] != 'B':
#                         w += 1
#                     if board[i][j] != 'W':
#                         b += 1
#         answer.append(w)
#         answer.append(b)

# print(min(answer))

# N, M = map(int, input().split())
# original = []
# count = []

# for _ in range(N):
#     original.append(input())

# for a in range(N-7):
#     for b in range(M-7):
#         index1 = 0
#         index2 = 0
#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))

# print(min(count))

n, m = map(int, input().split())
answer = []

def back():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
back()