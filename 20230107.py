# n = int(input())
# n = n % 8
# if n == 1 : print(1)
# elif n in [2,0]: print(2)
# elif n in [3,7]: print(3)
# elif n in [4,6]: print(4)
# elif n == 5: print(5)

# import math                     # lcm(), gcd()

# t = int(input())  # 최소공배수
# # aa = []
# # for _ in range(t):
# #     a,b = map(int, input().split())
# #     for i in range(max(a,b),(a*b)+1):
# #         if i % a == 0 and i % b == 0:
# #             aa.append(i)

# for _ in range(t):
#     a,b = map(int, input().split())
#     print(math.lcm(a,b))

# a,b,c = map(int, input().split())
# print(a+b+c)

# a = input()
# if a =='A+': print(4.3)
# elif a =='A0': print(4.0)
# elif a =='A-': print(3.7)
# elif a =='B+': print(3.3)
# elif a =='B0': print(3.0)
# elif a =='B-': print(2.7)
# elif a =='C+': print(2.3)
# elif a =='C0': print(2.0)
# elif a =='C-': print(1.7)
# elif a =='D+': print(1.3)
# elif a =='D0': print(1.0)
# elif a =='D-': print(0.7)
# else: print(0.0)

# t = int(input())
# for _ in range(t):
#     a = input()
#     print(a[0]+a[-1])

a,b = map(int, input().split())
print((a+b)*(a-b))