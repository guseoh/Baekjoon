# import sys

# n = int(sys.stdin.readline()) # 수 정렬하기3
# a = [0] * 10001
# for _ in range(n):
#     a[int(sys.stdin.readline())] += 1

# for i in range(10001):
#     if a[i] != 0:
#         for j in range(a[i]):
#             print(i)

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C == 0:
    num1 = A//C
else: num1 = (A//C) + 1
if B % D == 0:
    num2 = B//D
else: num2 = (B//D) + 1

num = max(num1,num2)
print(L-num)