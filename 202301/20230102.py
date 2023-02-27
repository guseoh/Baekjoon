# a,b,c = map(int, input().split()) #과자 한 개의 가격, 과자의 개수, 현재 가진 돈

# aa = a * b # 총 가격
# if(aa > c):
#     print(aa - c)
# else:
#     print(0)

# x = int(input()) # 소인수 분해
# d = 2

# while d <= x:
#     if x % d == 0:
#         print(d)
#         x = x / d
#     else:
#         d += 1

# a,b,c = map(int, input().split()) # 주사위 세개
# max = a
# if(a == b == c):
#     print((a*1000) + 10000)
# elif(a==b):
#     print(1000 + a*100)
# elif(a==c):
#     print(1000 + a*100)

# elif(b==c):
#     print(1000 + a*100)
# else:
#     print(100 * max(a,b,c))

# a = int(input())

# for i in range(a, 0, -1):
#     print("*" * i)

# a = int(input()) # 상근날드
# b = int(input())  
# c = int(input())
# d = int(input())
# e = int(input())

# print(min(a,b,c) + min(d,e) - 50)


# a = int(input())

# for i in range(1, a+1):
#     print("*" * i)

# t = int(input())

# for _ in range(t):
#     a,b = map(int, input().split())
#     print(a+b)

# a,b = map(int, input().split()) # X보다 작은 수
# num = list(map(int, input().split()))

# for i in range(a):
#     if num[i] < b:
#         print(num[i],end=' ')


# while 1:
#     a,b = map(int, input().split())
#     if a == 0 and b == 0:
#         break;
#     print(a+b)

# a = int(input()) #팩토리얼
# sum = 1
# for i in range(1,a+1):
#     sum *= i
# print(sum)

n = input()

print(sum(map(int, input())))