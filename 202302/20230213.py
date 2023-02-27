# import sys

# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# result = []

# def solution(x, y, N) :
#   color = paper[x][y]
#   for i in range(x, x+N) :
#     for j in range(y, y+N) :
#       if color != paper[i][j] :
#         solution(x, y, N//2)
#         solution(x, y+N//2, N//2)
#         solution(x+N//2, y, N//2)
#         solution(x+N//2, y+N//2, N//2)
#         return
#   if color == 0 :
#     result.append(0)
#   else :
#     result.append(1)


# solution(0,0,N)
# print(result.count(0))
# print(result.count(1))

# def hanoi(num,start,to,end):
#     if num == 1:
#         print(start, end)
#     else:
#         hanoi(num-1,start,end,to)
#         print(start, end)
#         hanoi(num-1,to,start,end)

# num = int(input())
# print(2 ** num - 1)
# hanoi(num,1,2,3)

import sys
import heapq
input = sys.stdin.readline

test = int(input())
heap = []

for i in range(test):
    num = int(input())
    if num != 0:
        heapq.heappush(heap,(-num)) # 최소 힙으로 구현 -> 최대 힙으로 변경
    else:
        try: # 가장 큰 값을 삭제하고 출력한다.
            print(-1 * heapq.heappop(heap))
        except: # 배열이 비어 있는 경우 0을 출력
            print(0)
