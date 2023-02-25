# import sys
# import heapq
# input = sys.stdin.readline

# test = int(input())
# heap = []

# for i in range(test):
#     num = int(input())
    
#     if num != 0:
#         heapq.heappush(heap,num) # 최소 힙
#     else:
#         try: 
#             print(heapq.heappop(heap))
#         except:
#             print(0)

# a,b = input().split()
# b = int(b)
# print(int(a,b))

# print(oct(int(input(), 2))[2:])

# system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# N, B = map(int, input().split())
# answer = ''

# while N != 0:
#     answer += str(system[N % B])
#     N //= B
# print(answer[::-1])


# arr = []
# for _ in range(int(input())):
#     arr.append(list(map(int, input().split())))
    
# arr.sort(key=lambda x:(x[0], x[1]))

# for i in arr:
#     print(str(i[0]) + " " + str(i[1]))


