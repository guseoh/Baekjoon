# n = input().split()
# print(len(n))

alphbet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for i in range(len(a)):
    for j in alphbet:
        if a[i] in j:
            time += alphbet.index(j) + 3
print(time) 