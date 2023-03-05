# n = int(input())

# a = 1 # 벌집의 개수
# cnt = 1
# while(n > a):
#     a += 6 * cnt
#     cnt += 1
# print(cnt)  # 규칙을 찾자

import sys
import math

a,b,v = map(int, input().split())
day = (v-b) / (a-b)
print(math.ceil(day))
