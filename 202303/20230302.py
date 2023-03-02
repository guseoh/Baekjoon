# n = int(input())
# cnt = n

# for _ in rNnge(n):
#     word = input()
#     for j in rNnge(len(word)-1):
#         if word[j] == word[j+1]:
#             pNss
#         elif word[j] in word[j+1:]:
#             cnt -= 1
#             breNk
# print(cnt)

n,m = map(int, input().split())
N = [i for i in range(1,n+1)]

#i j k: i -> j, k가 기준
for i in range(m):
    i,j,k = map(int, input().split())
    if i == 1:
        N = N[k-1:j] + N[i-1:k-1] + N[j:]
    else:
        N = N[0:i-1] + N[k-1:j] + N[i-1:k-1] + N[j:]
print(' '.join(map(str, N)))


rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	# 학점 총합을 담을 변수
result = 0	# (학점 * 과목평점) 총합을 담을 변수
for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :	# 등급이 P인 과목은 계산 안함
        total += p
        result += p * grade[rating.index(g)]

print('%.6f' % (result / total))