# import sys
# input = sys.stdin.readline

# n = int(input())
# a = []

# for i in range(n):
#     a.append((int(input()), i))

# max = 0
# sorted_A = sorted(a)

# for i in range(n):
#     if max < sorted_A[i][1] - i:
#         max =sorted_A[i][1] - i
# print(max+1)

# a = list(input())
# a.sort(reverse=True)

# for i in a:
#     print(i,end='')

# 프로그래머스 문자열 뒤집기               "".join() => 문자열 합치기

# a = list(input())

# for i in a[::-1]:
#     print(i,end='')

a = list(input())
n = input()
answer = []
for i in range(len(a)):
    if a[i] == n:
        continue
    answer.append(a[i])
for i in answer:
    print(i,end='')
    