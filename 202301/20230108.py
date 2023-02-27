# t = int(input())

# for _ in range(t):
#     tt = int(input())
#     num = 0
#     nnum = " "
#     for j in range(tt):
#         a, name = input().split()
#         a = int(a)
#         if num < a:
#             num = a
#             nnum = name
#     print(nnum)

# a = int(input())

# for i in range(1,a+1):
#     print(' '*(i-1) + '*' *(a-i+1) )

# for _ in range(3): 
#     aa = []
#     aa = list((map(int, input().split())))
#     c = aa.count(1)
#     if c == 1:print('C') # 1 한 개
#     elif c == 2:print('B') # 1 두 개
#     elif c == 3:print('A') # 1 세 개
#     elif c == 4:print('E') # 1 
#     else: print('D')

a = []
sum = 0
for i in range(5):
    n = int(input())
    a.append(n)
    a.sort()
    sum += a[i]
print(sum//5)
print(a[2])

