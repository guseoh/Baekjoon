# import sys
# input = sys.stdin.readline
# n = int(input())
# sum1 = 0
# for _ in range(n):
#     sum = 0
#     a = [0] * 3
#     a = list(map(int, input().split()))
#     a.sort()
    
#     if a[0] == a[1] or a[0] == a[2]:
#         if a[1] == a[2]: # 같은 눈 3개
#             sum = 10000 + a[0] * 1000
#         else: # 같은 눈 2개
#             if a[0] == a[1]:
#                 sum = 1000 + a[1] * 1000
#             else:
#                 sum = 1000 + a[2] * 1000
#     else:
#         sum = a[2] * 100
#     if sum > sum1:
#         sum1 = sum
# print(sum1)

# n = int(input())
# answer = 0

# for _ in range(n):
#     a,b,c = map(int, input().split())
#     if a == b == c:
#         answer = max(answer, 10000+a*1000)
#     elif a == b:
#         answer = max(answer, 1000+a*100)
#     elif a == c:
#         answer = max(answer, 1000+a*100)
#     elif b == c:
#         answer = max(answer, 1000+b*100)
#     else:
#         answer = max(answer, 100 * max(a,b,c))

# print(answer)

# t = int(input())

# for _ in range(t):
#     a,b = input().split()
#     a = int(a)
#     for i in b:
#         print(a * i,end='')
#     print()
    
# a = int(input())
# b = input()
# c = int(input())
# if b == '+':
#     print(a+c)
# else:
#     print(a*c)

n,m = map(int, input().split())
num = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= n and left <= right:
    sum1 = num[left:right]
    total = sum(sum1)
    
    if total == m:
        cnt += 1
        right += 1
    elif total < m:
        right += 1
    else: left += 1
print(cnt)