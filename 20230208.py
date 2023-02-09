# import math
# import sys
# input = sys.stdin.readline
# min, max = map(int, input().split())
# A = [0] * (int(max ** 0.5) + 1)

# for i in range(2,len(A)):
#     A[i] = i
# for i in range(2,int(math.sqrt(len(A))+ 1)):
#     if A[i] == 0: continue
#     for j in range(i+i,len(A),i):
#         A[j] = 0
# cnt = 0
# for i in range(2,int(max ** 0.5) + 1):
#     if A[i] != 0:
#         temp = A[i]
#         while A[i] <= max / temp:
#             if A[i] >= min / temp:
#                 cnt += 1
#                 temp = temp * A[i]
# print(cnt)


# import sys, math
# input = sys.stdin.readline

# m, n = map(int, sys.stdin.readline().split())

# primeList = [True] * (int(n ** 0.5) + 1)
# primeList[1] = False

# for i in range(2, int(n ** 0.5) + 1):
#     if primeList[i]:
#         if i * i > int(n ** 0.5):
#             break
#         for j in range(i**2, int(n ** 0.5) + 1, i):
#             primeList[j] = False

# count = 0
# for i in range(1, len(primeList)):
#     if primeList[i]:
#         res = i * i
#         while True:
#             if res < m:
#                 res *= i
#                 continue
#             if res > n:
#                 break
#             res *= i
#             count += 1

# print(count)

# import math
# n = int(input())
# a = [0] * (1000001)

# for i in range(2,len(a)):
#     a[i] = i

# for i in range(2,int(math.sqrt(len(a)) + 1)): # 제곱급까지
#     if a[i] == 0: 
#         continue
#     for j in range(i + i, len(a), i): # 배수 지우기
#         a[j] == 0

# def pal(target):
#     temp = list(str(target))
#     s = 0
#     e = len(temp) - 1
#     while (s < e):
#         if temp[s] != temp[e]:
#             False
#         s += 1
#         e -= 1
#     return True
# i = n

# while True:
#     if a[i] != 0:
#         result = a[i] 
#         if (pal(result)):
#             print(result)
#             break
#     i += 1
    
# import math

# def isPrime(x): # 소수인지 판별해주는 함수
#     for i in range(2, int(math.sqrt(x)+1)):
#         if x % i == 0:
#             return False
#     return True

# N = int(input())
# result = 0

# for i in range(N, 1000001): # 입력값 N 부터 최대값 까지 순환
#     if i == 1: # 1은 소수가 아니기 때문에 예외처리
#         continue
#     if str(i) == str(i)[::-1]: # 팰림드롬 수 일 경우
#         if isPrime(i) == True: # 소수 판별 함수 적용
#             result = i
#             break

# if result == 0: # 입력값이 만약 최대 값 100만일 경우
#     result = 1003001 # 100만 이상이면서 팰림드롬 및 소수일 경우를 적용

# print(result)

# n = input()
# num = n
# cnt = 0
# while 1:
#     if len(num) == 0:
#         num = "0" + num
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     cnt += 1
#     if num == n:
#         print(cnt)
#         break

n = int(input())
num = n
cnt = 0
while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b * 10) + c
    cnt += 1
    if num == n:
        print(cnt)
        break
