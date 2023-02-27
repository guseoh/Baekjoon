# 지금[n] = 지금[n-3] + 포도주[n] + 포도주[n-1]
# 지금[n] = 지금[n-2] + 포도주[n]
# 지금[n] = 지금[n-1]

# dp = [0] * 10001 # 지금
# glass = [0] * 10001 # 포도주

# n = int(input())
# for i in range(1, n+1):
#     glass[i] = int(input())

# dp[1] = glass[1] # 첫 번째 포도주 잔
# dp[2] = glass[1] + glass[2] # 첫 번째 포도주 잔 + 두 번째 포도주 잔
# for i in range(3, n+1):
#     dp[i] = max(dp[i-1], dp[i-2] + glass[i], dp[i-3] + glass[i] + glass[i-1])

# print(dp[n])

# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# dp = [1] * N

# for i in range(1,N):
#     for j in range(i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    avg, cnt= 0, 0
    a = list(map(int, input().split()))
    avg = sum(a[1:]) // a[0]
    for score in a[1:]:
        if score > avg:
            cnt += 1
    rate = 100 * (cnt / a[0])
    print(f'{rate:.3f}%')