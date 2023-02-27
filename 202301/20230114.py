# dish = list(str(input()))
# answer = 0

# for i in range(len(dish)):
#     if i == 0:
#         answer += 10
#     elif dish[i] == dish[i-1]:
#         answer += 5
#     else: answer += 10
# print(answer)

t = int(input())
aa,bb = 0,0
for _ in range(t):
    for i in range(9):
        a,b = map(int, input().split())
        aa += a
        bb += b
    if aa > bb:
        print("Yonsei")
    elif aa < bb:
        print("Korea")
    else:
        print("Draw")