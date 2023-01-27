import math

# a = 10
# b = 8
# g = math.gcd(a,b)
# print(g)

# s = "pppy"
# for i in range(len(s)):
#     a,b,c,d = 0,0,0,0
#     sum1, sum2 = 0, 0
#     a += s.count("p")
#     b += s.count("P")
#     c += s.count("y")
#     d += s.count("Y")
#     sum1 = a+b
#     sum2 = c+d

# x % sum([int(i) for i in str(x)]) == 0


# def solution(n):
#     x = [int(i) for i in str(n)]
    
#     return x[::-1]

# n = int(input())
# count = 0
# start = 0
# end = 0

# for i in range(2,n+1):  # 소수 판별
#     for j in range(2, i+1):
#         if j == i:
#             ss.append(i)
#         if i % j == 0:
#             break

# # 애라토스테네서의 채
# a = [False, False] + [True] * (n-1) # 소수는 2부터
# ss = []
# for i in range(2, n+1):
#     if a[i]:
#         ss.append(i)
#         for j in range(2*i, n+1, i):
#             a[j] = False
            
# while end <= len(ss):
#     sum1 = sum(ss[start:end])
#     if sum1 == n:
#         count += 1
#         end += 1
#     elif sum1 < n:
#         end += 1
#     else: start += 1
# print(count)

# a,b = map(int, input().split())
# for i in range(a,b+1):
#     if i == 1: continue
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else: print(i)

# checklist = [0] * 4
# mylist = [0] * 4
# checksecret = 0

# def myadd(c):
#     global checklist, mylist, checksecret
#     if c == 'A':
#         mylist[0] += 1
#         if mylist[0] == checklist[0]:
#             checksecret += 1
#     elif c == 'C':
#         mylist[1] += 1
#         if mylist[1] == checklist[1]:
#             checksecret += 1
#     elif c == 'G':
#         mylist[2] += 1
#         if mylist[2] == checklist[2]:
#             checksecret += 1
#     elif c == 'T':
#         mylist[3] += 1
#         if mylist[3] == checklist[3]:
#             checksecret += 1
            
# def myremove(c):
#     global checklist, mylist, checksecret
#     if c == 'A':
#         if mylist[0] == checklist[0]:
#             checksecret -= 1
#         mylist[0] -= 1
#     elif c == 'C':
#         if mylist[1] == checklist[1]:
#             checksecret -= 1
#         mylist[1] -= 1
#     elif c == 'G':
#         if mylist[2] == checklist[2]:
#             checksecret -= 1
#         mylist[2] -= 1
#     elif c == 'T':
#         if mylist[3] == checklist[3]:
#             checksecret -= 1
#         mylist[3] -= 1

# s,p = map(int, input().split())
# result = 0
# A = list(input())
# checklist = list(map(int, input().split()))

# for i in range(4):
#     if checklist[i] == 0:
#         checksecret += 1
        
# for i in range(p):
#     myadd(A[i])
#     if checksecret == 4:
#         result += 1
        
# for i in range(p,s):
#     j = i - p
#     myadd(A[i])
#     myremove(A[j])
#     if checksecret == 4:
#         result += 1
# print(result)

# s = []
# for i in range(5):
#     a = int(input())
#     s.append(a)
# s.sort()
# print(sum(s) // 5)
# print(s[2])

one = 0
two = 0
a = []

for _ in range(9):
    a.append(int(input()))
s = sum(a)

for i in range(8):
    for j in range(i+1,9):
        if s - (a[i]+a[j]) == 100:
            one = a[i]
            two = a[j]
a.remove(one)
a.remove(two)
a.sort()
for i in a:
    print(i)