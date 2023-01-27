
# swapcase()  # 대소문자 바꿔준다

# for i in input():
#     if i.isupper():
#         print(i.lower(), end='')
#     else:
#         print(i.upper(), end='')

# for i in input():
#     a = int(i)
#     print(a.sort())

# a,b,c,d,e,f = map(int, input().split()) # 킹, 퀸, 룩, 비숍, 나이트, 폰
# print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)

# h,m = map(int, input().split())

# if m >= 45:
#     print(h,m-45)
# elif h > 0 and min < 45:
#     print(h-1, m+15)
# else:
#     print(23, m+15)
    
# hour, min = map(int,input().split())

# if min >= 45:
#     print(hour, min-45)
# elif hour>0 and min < 45:
#     print(hour-1, min+15)
# else:
#     print(23, min+15)

# a = int(input()) # 영수증
# t = int(input()) # 물건의 종류의 수
# sum = 0
# for i in range(t):
#     b1, b2 = map(int, input().split())
#     sum = sum + (b1 * b2)
    
# if a == sum:
#     print('Yes')
# else: print('No')

s = [i for i in range(1,31)]

for _ in range(28):
    a = int(input())
    s.remove(a)
print(min(s))
print(max[s])