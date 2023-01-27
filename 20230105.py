# a = list(input())  # find() 함수 이용 - 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력
# s = 'abcdefghijklmnopqrstuvwxyz'

# for i in s:
#     if i in a:
#         print(a.index(i), end=' ')
#     else:
#         print(-1, end=' ')

# while True: # 예외처리
#     try:
#         print(input())
#     except:
#         break

# a, b = map(int, input().split())
# print(a+b)

# a, b = map(int, input().split())
# print(abs(a-b))

# print('고려대학교')

# a,b = map(int, input().split()) # 엄청난 부자2
# print(a//b)
# print(a%b)

# A,B = [], []

# a,b = map(int, input().split())
# for i in range(a):
#         i = list(map(int, input().split()))
#         A.append(i)
# for i in range(a):
#         i = list(map(int, input().split()))
#         B.append(i)
# for i in range(a):
#     for ii in range(b):
#         print(A[i][ii] + B[i][ii],end=' ')
#     print()

        
t = int(input())

for i in range(t):
        a = input()
        a = a[0].upper() + a[1:]
        print(a)
