# aa,ab,ac = map(int, input().split())
# ca,cb,cc = map(int, input().split())
# print(ca-ac, cb//ab, cc-aa)

# a = input()
# print("Avengers: Endgame")

# a = int(input())
# c = int(a * (8/10)) 
# print(int(a-(a*(0.22))), c + int(((a-c) - (a - c) * 0.22)))

# a = int(input())
# print('A')

# a = int(input())
# aa = "long " * (a // 4)
# print(aa, end='')
# print("int")

t = int(input())
for _ in range(t):
    a = list(input())
    if len(a) >= 6 and len(a) <= 9:
        print("yes")
    else: print("no")