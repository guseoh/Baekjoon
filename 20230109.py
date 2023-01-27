import sys

t = int(sys.stdin.readline())
a = []
for _ in range(t):
    a.append(int(sys.stdin.readline()))
a.sort()
for i in a:
    print(i)
