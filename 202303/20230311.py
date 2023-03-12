# arr = []
# for _ in range(int(input())):
#     arr.append(list(map(int, input().split())))
    
# arr.sort(key=lambda x:(x[0], x[1]))

# for i in arr:
#     print(str(i[0]) + " " + str(i[1]))

# arr = []
# for _ in range(int(input())):
#     arr.append(list(map(int, input().split())))

# arr.sort(key=lambda x:(x[1], x[0]))

# for i in arr:
#     print(str(i[0]) + " " + str(i[1]))

# n = int(input())
# a = list(map(int, input().split()))

# a2 = sorted(list(set(a)))
# dic = {a2[i] : i for i in range(len(a2))}
# for i in a:
#     print(dic[i], end=' ')

n = int(input())
a = list(map(int, input().split()))
y = m = 0

for i in a:
    y += (n // 30 + 1) * 10
    m += (n // 60 + 1) * 15
if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else: 
    print("Y", y)

N = int(input())
li = list(map(int, input().split()))
y = m = 0
for n in li:
    y += (n//30 + 1) * 10
    m += (n//60 + 1) * 15
if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else:
    print("Y", y)