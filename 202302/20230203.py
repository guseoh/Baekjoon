# sum1 = 0
# cnt = 0
# for i in range(5):
#     x  = 0
#     a = [0,0,0,0,0]
#     a= list(map(int, input().split()))
#     x = sum(a)
#     if x > sum1:
#         sum1 = x
#         cnt = i
# print((cnt+1),sum1)


a = [sum(list(map(int, input().split()))) for i in range(5)]
print(a.index(max(a)) + 1, max(a))