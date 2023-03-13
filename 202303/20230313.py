from collections import deque
stack = deque()
for i in range(int(input())):
    
    a = list(input().split())
    
    if a[0] == "push_back":
        stack.append(int(a[0]))
    elif a[0] == "push_front":
        stack.appendleft(a[0])
    elif a[0] == "pop_front":
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack.popleft())
    elif a[0] == "pop_back":
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack) <= 0:
            print(0)
        else: 
            print(1)
    elif a[0] == "front":
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[0])
    elif a[0] == "back":
        if len(stack) <= 0:
            print(-1)
        else:
            print(stack[-1])