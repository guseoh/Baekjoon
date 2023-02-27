import sys
input = sys.stdin.readline

# a = int(input())
# aa = []
# for i in range(a):
#     aa.append(int(input()))
# b = int(input())
# bb = []
# for i in range(b):
#     bb.append(int(input()))

# for i in range(b):
#     for j in range(a):
#         if aa[j] == bb[i]:
#             print(1)
#         else: break
#     print(0)
    
    
# aa = []
# for i in range(5):
#     a = list(int(input()))
# print(a)

# N = int(input())
# chicken = list(map(int, input().split()))
# result = 0

# for i in range(3) :
#     if chicken[i] <= N :
#         result += chicken[i]
#     else :
#         result += N

# print(result)

def solution(n):
    nList = list(map(int, str(n)))
    newL = sorted(nList, reverse = True)
    strings = [str(i) for i in newL]
    a_string = "".join(strings)

    return int(a_string)

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))