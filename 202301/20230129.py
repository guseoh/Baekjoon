# n = int(input())
# for i in range(1,n+1):
#     print(" " * (n-i) + "*" * (2 * i - 1))

# while True:
#     a,b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
    
#     if a % b == 0:
#         print("multiple")
#     elif b % a == 0:
#         print("factor")
#     else: print("neither")

a,i = map(int, input().split())
print(a * (i - 1)+ 1)

