from collections import deque

n, m, start = map(int, input().split())
A = [ [] for _ in  range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n+1): # 번호가 작은 노드부터 방문하기 위해 정렬
    A[i].sort()

def DFS(v):
    print(v,end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
visited = [False]  * (n+1)
DFS(start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
print()
visited = [False] * (n+1)
BFS(start)