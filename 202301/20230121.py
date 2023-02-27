# a = int(input()) # 별 찍기 - 20
# for i in range(1,a):
#     if i % 2 == 0:
#         print() 
import sys
input = sys.stdin.readline


a,b = map(int, input().split())
aa = []
for i in range(1,a+1):
    if a % i == 0:
        aa.append(i) 

if len(aa) < b:
    print(0)
else:
    print(aa[b-1])