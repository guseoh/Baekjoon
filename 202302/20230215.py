# BFS => Queue, DFS => 재귀함수
# def dfs(idx, sum):
#     global answer
#     if(idx >= n):
#         return
#     sum += arr[idx]
#     if(s == sum):
#         answer += 1
#     dfs(idx+1, sum - arr[idx])
#     dfs(idx+1, sum) 
    
# n,s = map(int, input().split())
# arr = list(map(int, input().split()))
# answer = 0
# dfs(0,0)
# print(answer)

# n,k = list(map(int, input().split()))

# up = 1
# for i in range(1, n+1): # n!
#     up *= i

# down = 1
# for i in range(1, n-k+1): # (n-k)!
#     down *= i

# down2 = 1
# for i in range(1,k+1): # k!
#     down2 *= i

# down *= down2 # (n-k)! * k!
# print(up // down)

def LCM(a, b):
    return (a * b) // GCD(a, b)
def GCD(a, b): # 유클리드 호제법
    if b % a:
        return GCD(b % a, a)
    else: return a

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(LCM(a,b))
