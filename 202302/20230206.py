# a,b = map(int, input().split())
# ls = []

# for _ in range(a):
#     ls.append(int(input()))
# ls.reverse() # 내림차순
# cnt = 0
# for i in range(a):
#     if b >= ls[i] :
#         cnt += b // ls[i]
#         b = b % ls[i]
# print(cnt)

# from queue import PriorityQueue
# n = int(input())
# pq = PriorityQueue()

# for _ in range(n): # 우선순위 큐 데이터 삽입
#     data = int(input())
#     pq.put(data)
# d1, d2 = 0, 0
# sum = 0
# while pq.qsize() > 1:
#     d1 = pq.get()
#     d2 = pq.get()
#     temp = d1 + d2
#     sum += temp
#     pq.put(temp)
# print(sum)

# a = input().split('-')
# num = []
# for i in a:
#     sum = 0
#     s = i.split('+')
#     for j in s:
#         sum += int(j)
#     num.append(sum)
# n = num[0]
# for i in range(1,len(num)):
#     n -= num[i]
# print(n)

# str = input() # 문자열 추출
# result = str
# for char in str:
#     if char in "aeiou":
#         result = result.replace(char, '')

# print(result)

# answer = ""  # 대소문자 바꾸기
# for i in input():
#     if i.islower():
#         answer += i.upper()
#     else:
#         answer += i.lower()
# print(answer)

cipher = list(input())
code = int(input())
answer = ''
for i in range(code-1, len(cipher),code):
    answer += cipher[i]
print(answer)
