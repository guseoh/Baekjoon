# t = int(input())

# for i in range(t):
#     k = int(input()) # 층
#     n = int(input()) # 호
#     people = [i for i in range(1,n+1)]
    
#     for x in range(k):
#         new = []
#         for y in range(n):
#             new.append(sum(people[:y+1]))
#         people = new.copy()
#     print(people[-1])

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     a,b = map(int, input().split())
    
#     print(a ** b % 10)

# t = int(input())

# for _ in range(t):
#     a,b = map(int, input().split())
#     a = a % 10
#     # 각 숫자 제곱 ->  일의 자리
#     if a == 0: # 10
#         print(10)
#     elif a == 1 or a == 5 or a == 6: 
#         print(a)
#     elif a== 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a * a) % 10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a**4) % 10 % 10 % 10)
#         else:
#             print((a**b) % 10 % 10 % 10)

# a = list(map(str, input().split()))
# c = a[0]+a[1]
# d = a[2]+a[3]
# print((int(c) + int(d)))

n = int(input())
