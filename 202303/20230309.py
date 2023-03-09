# a = input()
# b = int(input())
# print(a[b-1])

# a,b = map(int, input().split())
# aa = list(map(int, input().split()))
# aa.sort()
# print(aa[-b])

from collections import Counter # Counter
import sys
imput = sys.stdin.readline

a = []
for _ in range(int(input())):
    x = int(input())
    a.append(x)
    
a.sort()

print(sum(a) // len(a))
print(a[len(a)//2])

cnt = Counter(a).most_common(2)

if len(a) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else: print(cnt[0][0])

print(max(a) - min(a)) 
