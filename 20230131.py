# m = int(input())
# n = int(input())

# a = []
# for i in range(m,n+1):
#     error = 0
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 error += 1
#                 break
#         if error == 0:
#             a.append(i)
# if len(a) == 0:
#     print(-1)
# else:
#     print(sum(a))
#     print(min(a))
    

# a = int(input())
# aa = []
# for i in range(a):
#     x = int(input())
#     aa.append(x)
#     aa.sort()
# for i in aa:
#     print(i)

# hp = int(input())

# hp1 = hp % 5
# hp2 = hp1 % 3
# print((hp // 5) + (hp1 // 3) + hp2)

def solution(rsp: str) -> str:
    dict = {"2": "0", "0": "5", "5": "2"}
    
    return "".join(map(str, [dict[x] for x in rsp]))

    