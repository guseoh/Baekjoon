

# n = int(input())
# arr = list(map(int, input().split()))
# stack = []
# answer = [-1 for i in range(n)]

# for i in range(len(arr)):
#     while stack and arr[stack[-1]] < arr[i]:
#         answer[stack.pop()] = arr[i]
#     stack.append(i)
# print(*answer) # 배열을 print, *을 붙여주면 공백을 기준으로 원소들만 나열한다.

# import sys
# input = sys.stdin.readline

# k = int(input())
# stack = []

# for i in range(k):
#     a = int(input())
#     if a == 0:
#         stack.pop()
#     if a != 0:
#         stack.append(a)

# print(sum(stack))

# from collections import deque
# n = int(input())
# myqueue = deque()

# for i in range(1,n+1):
#     myqueue.append(i)
# while len(myqueue) > 1:
#     myqueue.popleft()
#     myqueue.append(myqueue.popleft())
# print(myqueue[0])

from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
myqueue = PriorityQueue() # 우선 순위 큐

for i in range(n):
    a = int(input())
    if a == 0:
        if myqueue.empty():
            print('0\n')
        else:
            temp = myqueue.get()
            print(str(temp([1])) + '\n')
    else:
        myqueue.put((abs(a),a))
    