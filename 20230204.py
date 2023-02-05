# from collections import deque

# n, m, start = map(int, input().split())
# A = [ [] for _ in  range(n+1)]
# for _ in range(m):
#     s,e = map(int, input().split())
#     A[s].append(e)
#     A[e].append(s)

# for i in range(n+1): # 번호가 작은 노드부터 방문하기 위해 정렬
#     A[i].sort()

# def DFS(v):
#     print(v,end=' ')
#     visited[v] = True
#     for i in A[v]:
#         if not visited[i]:
#             DFS(i)
            
# visited = [False]  * (n+1)
# DFS(start)

# def BFS(v):
#     queue = deque()
#     queue.append(v)
#     visited[v] = True
#     while queue:
#         now = queue.popleft()
#         print(now, end=' ')
#         for i in A[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
# print()
# visited = [False] * (n+1)
# BFS(start)

# from collections import deque
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# n,m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
# visited = [[False] * m for _ in range(n)]

# for i in range(n):
#     num = list(input())
#     for j in range(m):
#         a[i][j] = int(num[j])
# def BFS(i,j):
#     queue =deque()
#     queue.append((i,j))
#     visited[i] == True
#     while queue:
#         now = queue.popleft()
#         for k in range(4):
#             x = now[0] + dx[k]
#             y = now[1] + dy[k]
#             if x >= 0 and y >= 0 and x < n and y < m:
#                 if a[x][y] != 0 and not visited[x][y]:
#                     visited[x][y] = True
#                     a[x][y] = a[now[0]][now[1]] + 1
#                     queue.append((x,y))
# BFS(0,0)
# print(a[n-1][m-1])

