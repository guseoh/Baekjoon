import sys
import heapq
input = sys.stdin.readline

test = int(input())
heap = []

for i in range(test):
    num = int(input())
    
    if num != 0:
        heapq.heappush(heap,num) # 최소 힙
    else:
        try: 
            print(heapq.heappop(heap))
        except:
            print(0)
