# a = int(input())

# for i in range(a):
#     print(" " * i,end='')
# for j in reversed(range(1,a+1)):
#     print('*' * j )



# while True:
#     a,b,c = map(int, input().split())
#     if a == 0 and b == 0 and c == 0:
#         break
#     num = [a,b,c]
#     num.sort()
#     if (num[0] ** 2) + (num[1] ** 2) == num[2] ** 2:
#         print('right')
#     else: print('wrong')

# a = input()
# for i in range(0, len(a),10):
#     print(a[i:i+10])  # range(시작값, 종료값, step)

# x,y,w,h = map(int, input().split())
# print(min(x,y,w-x,h-y))

# while True:
#     a,b =  map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# aa = []
# t = int(input())
# for _ in range(t):
#     a = int(input())
#     aa.append(a)
# if aa.count(1) > aa.count(0):
#     print('Junhee is cute!')
# else:
#     print('Junhee is not cute!')

t = int(input())

for _ in range(t):
    Name =" "
    N = 0
    nn = int(input())
    for i in range(nn):
        name, n = input().split()
        n = int(n)
        if n > N:
            N = n
            Name = name
    print(Name)