# a = int(input())

# for _ in range(a):
#     n = int(input())
#     if n % 2 == 0: print('even')
#     else: print('odd')

n = list(map(int, input().split()))
abc = list(input())
n.sort()
for i in abc:
    if i == "A":
        print(n[0],end=" ")
    elif i == "B":
        print(n[1], end=" ")
    else: print(n[2],end=" ")
    
    