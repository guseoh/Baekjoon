import sys
input = sys.stdin.readline

# sum = 0
# temp = [0]
# N,M = map(int, input().split())
# numbers = list(map(int, input().split()))

# for j in range(N):
#     sum += numbers[j]
#     temp.append(sum)
# for i in range(M):
#     start, end= map(int, input().split())
#     print(temp[end] - temp[start-1]) 

# n,m = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(n)]
# D = [[0] * (n+1) for i in range(n+1)]

# for i in range(1, n+1): # 누적 합
#     for j in range(1, n+1):
#         D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i-1][j-1]
# for _ in range(m):
#     a,b,c,d = map(int, input().split())
#     print(D[c][d] - D[a-1][d] - D[c][b-1] + D[a-1][b-1])

# sum = []
# temp = 0
# a = list(map(int, input().split()))
# for i in a:
#     temp += i
#     sum.append(temp)
# print(sum)

n,m = map(int, input().split())
a = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = a[0]
answer = 0
for i in range(1,n):
    S[i] = S[i-1] + a[i]
for i in range(n):
    re = S[i] % m
    if re == 0:
        answer +=1
    C[re] += 1
for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)
print(answer)

s = 0
for i in input().split():s+=int(i);s%=m;a[s]+=1
