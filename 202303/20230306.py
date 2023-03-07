# while True:
#     n = int(input())
#     if n == -1:
#         break
    
#     a = []
#     for i in range(1,n):
#         if n % i == 0:
#             a.append(i)
    
#     if sum(a) == n:
#         print(n, "=", " + ".join(map(str, a)))
#     else:
#         print(n, "is NOT perfect.")

# n = int(input())
# line = 1

# while n > line:
#     n -= line
#     line += 1
# if line % 2 == 0:
#     up = n
#     down = line - n + 1
# else:
#     up = line - n + 1
#     down = n
# print(up, '/',down, sep="")

# a,b = map(int, input().split())
# print(a+b)

# import datetime
# now = datetime.datetime.now() + datetime.timedelta(hours=9)
# print(now.year)
# print(now.month)
# print(now.day)

# n = int(input())

# if  n % 5 == 0:
#     print(n // 5)
# else: print(n // 5 + 1)

m = 6790
a= [500, 100, 50, 10]
cnt = 0
for i in range(len(a)):
    s = m // a[i]
    cnt += s
    m = m - s * a[i]
print(cnt)
