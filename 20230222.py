# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# if sum(a) >= sum(b):
#     print(sum(a))
# else: print(sum(b))

# import sys
# input = sys.stdin.readline
# a = int(input())
# b = int(input())
# c = int(input())

# if (a + b + c) == 180:
#     if a == b or a == c or b == c:
#         print("Isosceles")
#     elif a == b == c == 60:
#         print("Equilateral") 
#     else:
#         print("Scalene")
# else:
#     print("Error")

# a, b= map(int, input().split())
# n = list(map(int, input().split()))
# z = []

# for i in n:
#     z.append(i -(a * b))
    
# print(' '.join(map(str, z)))

# while(True):
#     a = input()
#     if a == 'END':
#         break
#     print(''.join(a[::-1]))

a, b= map(int, input().split())
c, d= map(int, input().split())
print(min(a+d, c+b))