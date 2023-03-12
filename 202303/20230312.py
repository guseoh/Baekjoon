a,b = map(int, input().split())
z = list(map(int, input().split()))
s = 0
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1,a):
            if z[i] + z[j] + z[k] > b:
                continue
            else:
                s = max(s,z[i] + z[j] + z[k])
print(s)