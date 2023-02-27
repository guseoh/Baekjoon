# n = int(input())
# a = list(map(int, input().split()))

    
# a.sort()
# sum1 = [0] * n
# sum1[0] = a[0]
# for j in range(1,n):
#     sum1[j] = sum1[j-1] + a[j]
# print(sum(sum1))

# a,b = map(int, input().split())
# aa = list(map(int, input().split()))
# aa.sort()
# print(aa[b-1])

# n = int(input())
# li = list(map(int, input().split()))
# count = 0

# for i in range(n):
#     error = 0
#     if li[i] > 1:
#         for j in range(2,li[i]):
#             if li[i] % j == 0:
#                 error += 1
#         if error == 0:
#             count += 1

# print(count)

# em = list(map(int, input().split()))
# aa = []
# for i in range(len(em)):
#     aa.append(em.index(em[i]))
# print(aa)

def solution(n):  # extend
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])
    return len(answer)