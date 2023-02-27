# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# a = input()

# for i in croatia:
#     a = a.replace(i, '*')
# print(len(a))

# while(True):
#     cnt = 0
#     n = input()
#     n.lower()
#     if n == '#':
#         break
#     for i in n:
#         if i in 'aeiou':
#             cnt += 1 
#     print(cnt)
    
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# while True:
#     line = input()
#     if line == '#': break
#     print(sum([(ch in vowels) for ch in line]))

#9 7 5 3 1   0 1 2 3 4 
# n = int(input())
# for i in range(n, 0, -1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))

# a = [int(input()) for _ in range(4)]
# a.sort()
# b = [int(input()) for _ in range(2)]
# # print(sum(a[1:]) + max(b))

# n = int(input())
# a = [str(i) for i in range(1,n+1)]
# c = []
# for i in a:
#     if i == '4' or i == '7':
#         c.append(i)
# print(c)


n = int(input())
while True:
    flag = True
    for i in str(n):
        print(i)
        if i!="4" and i!="7":
            flag = False
            n -= 1
    if flag :
        print(n)
        break
