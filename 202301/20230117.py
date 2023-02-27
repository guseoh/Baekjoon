# n = int(input())
# count = 1
# start = 1
# end = 1
# sum = 1

# while end != n:
#     if sum == n:
#         count += 1
#         end += 1
#         sum += end
#     elif sum > n:
#         sum -= start
#         start += 1
#     else:
#         end += 1
#         sum += end
# print(count)

# n = int(input())
# num = int(input())
# count = 0
# a = list(map(int, input().split()))
# a.sort()
# start = 0
# end = n-1

# while start < end:
#     if a[start] + a[end] < num:
#         start += 1
#     elif a[start] + a[end] > num:
#         end -= 1
#     else: 
#         count += 1
#         start += 1
#         end -= 1
# print(count)

a,b = map(int, input().split()) # a개의 수, b가 되는 경우     # BOJ 2003
aa = list(map(int, input().split()))
count = 0
start = 0
end = a-1
aa.sort()

while start < end:
    if aa[start] + aa[end] < b:
        start += 1
    elif aa[start] + aa[end] > b:
        end -= 1
    else:
        count += 1
        if aa[start] == aa[end]:
            start += 1
        else:
            start += 1
            end -= 1
        
print(count)

# import sys
# input = sys.stdin.readline
# n = int(input())
# result = 0
# A = list(map(int, input().split()))
# A.sort()

# for k in range(n):
#     find = A[k]
#     i = 0
#     j = n - 1
#     while i < j:
#         if A[i] + A[j] == find:
#             if i != k and j != k: #
#                 result += 1
#                 break
#             elif i == k:
#                 i += 1
#             elif j == k:
#                 j -= 1
#         elif A[i] + A[j] < find:
#             i += 1
#         else:
#             j -= 1
# print(result)

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         sum += i
# print(sum)

# a = list(map(int, input().split()))
# print(min(a),max(a))
