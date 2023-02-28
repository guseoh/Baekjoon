# deque: 스택 + 큐
from collections import deque

s = deque()
n, k = map(int, input().split())
for i in range(1,n+1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k-1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')

# put: 추가, get: 삭제
import sys
from collections import deque
q = deque()
input = sys.stdin.readline

for i in range(int(input())):
    s = []
    s = input().split()

    if s[0] == 'push':
        q.append(int(s[1]))
    elif s[0] == 'front':
        if not q: print(-1)
        else:print(q[0])
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q: print(1)
        else: print(0)
    elif s[0] == 'back':
        if not q: print(-1)
        else:print(q[-1])
    elif s[0] == 'pop':
        if not q: print(-1)
        else: print(q.popleft())

T = int(input())

for i in range(T):
    h, w, n = map(int, input().split( )) # h=각 호텔의 층 수, w=각 층의 방 수, n=몇 

    floor = n % h 
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)