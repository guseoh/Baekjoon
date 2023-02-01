# # 진료순서 정하기
# a = list(map(int, input().split()))
# answer = []
# aa = sorted(a)
# aa.reverse()

# for i in a:
#     answer.append(aa.index(i)+1)
# print(answer)

# n,m = map(int, input().split())
# print(n * m - 1)

# aa = []
# a = list(input())
# for i in a[::-1]:
#     aa.append(i)
# if a == aa:
#     print(1)
# else: print(0)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i) # 재귀
count = 0
for i in range(1,n+1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count)
