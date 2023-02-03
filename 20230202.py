# import re
# a = []
# sum = 0
# ss = "abc1adad2"
# num = re.sub(r'[^0-9]','',ss)
# for i in num:
#     sum += int(i)

# print(sum)

# import sys
# input = sys.stdin.readline

# n = int(input())
# answer = list(map(int, input().split()))

# nn = int(input())
# answer2 = list(map(int, input().split()))

# for i in answer2:
#     cnt = 0
#     for j in range(n):
#         if answer[j] == i:
#             cnt += 1
#             break
#     if cnt != 0:
#         print(1)
#     else: print(0)

# import sys
# input = sys.stdin.readline
# n = int(input())
# answer = set(map(int, input().split()))
# nn = int(input())
# answer2 = list(map(int, input().split()))

# for i in answer2:
#     print(1) if i in answer else print(0)

# set() 자료형으로 문자열 중북 제거
n = int(input())
a = [str(input()) for i in range(n)] # 문자열 반복 입력
a = list(set(a))
a.sort()
a.sort(key=len)
print("\n".join(a))