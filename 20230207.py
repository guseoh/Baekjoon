# n = int(input())
# s, cnt = 0, 0
# for i in range(n):
#     a,b = map(int, input().split())
#     if a > s:
#         s = b
#         cnt += 1
# print(cnt)

import sys
input = sys.stdin.readline
n = int(input())
meet = []
for i in range(n):
    a,b = map(int, input().split())
    meet.append([a,b])

meet.sort(key=lambda x:(x[1],x[0]))  # x[1] 오름차순 -> 같을 경우 x[0] 비교

answer = 0
end = 0

for i in range(n):
    if end <= meet[i][0]:
        end = meet[i][1]
        answer += 1
print(answer)
