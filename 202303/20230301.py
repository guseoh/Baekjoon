# import math
# n = int(input())
# result = n

# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         result -= result / i
#         while n % i == 0:
#             n /= i
# if n > 1:
#     result -= result / n
# print(int(result))

# n, m = map(int, input().split())
# a = [0 for _ in range(n)]

# for b in range(m):
#     i,j,k = map(int, input().split())
#     for c in range(i,j+1):
#         a[c-1] = int(k)
# print(' '.join(map(str, a)))

# i,j = map(int, input().split())
# a = [c for c in range(1,i+1)]
# for _ in range(j):
#     tmp = 0
#     n,m = map(int, input().split())

#     tmp = a[n-1]
#     a[n-1] = a[m-1]
#     a[m-1] = tmp

# print(' '.join(map(str, a)))
import sys
input = sys.stdin.readline

i,j = map(int, input().split())
a = [c for c in range(1,i+1)]

for _ in range(j):
    n,m = map(int, input().split())
    a = a[:n-1] + a[n-1:m][::-1]+ a[m:]

print(' '.join(map(str, a)))