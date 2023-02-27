# divmod == print(a//b, a%b)

# 진법 바꾸기
num = '3212'
base = 5
answer = int(num, base)

# 문자열 정렬하기
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

# 알파벳 출력하기
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

# 새로운 정렬된 리스트
list1 = [3, 2, 5, 1]
list2 = sorted(list1)

# zip 함수
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))

# zip => 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수
list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]

# map함수 
list1 = ['1', '100', '33']
list2 = list(map(int, list1))

# 곱집합
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))

num = set(range(1, 10000))
rev = set()

for n in num:
    for j in str(n):
        n += int(j)
    rev.add(n)
se = num - rev
for i in sorted(se):
    print(i)

# 순열과 조합
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) 
print(list(map(''.join, itertools.combinations(pool, 2))))

# import itertools

# def solution(mylist):
#     answer = []
#     answer = ''.join(map(str, itertools.permutations(mylist)))
#     return answer

from itertools import permutations
def solution(mylist):
    return sorted(list(permutations(mylist, len(mylist))))

def permute(mylist):
    result = [mylist[:]]
    c = [0] * len(mylist)
    i = 0
    while i < len(mylist):
        if c[i] < i:
            if i % 2 == 0:
                mylist[0], mylist[i] = mylist[i], mylist[0]
            else:
                mylist[c[i]], mylist[i] = mylist[i], mylist[c[i]]
            result.append(mylist[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1


# 가장 많은 알파벳 찾기
import collections

my_str = input().strip() # 입력
answer = collections.Counter(my_str) # Counter(C 대문자), 딕셔너리 형태로 저장
values = [i for i in answer.values()]
values.sort(reverse=True)
big = values[0]

result = [i for i,k in answer.items() if big==k] # 간단히 하기
result = ''.join(sorted(result))
print(result)


# flag OR for-else
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')

# Swap
a = 3
b = 'avs'
a,b = b,a

# 이진 탐색
import bisect
mylist = [1,2,3,4,5,6]
print(bisect.bisect(mylist,3))

# 가장 큰 수, inf (양의 무한대), -inf (음의 마한대)
min = float('inf')
min > 1000000000

n = int(input())
for i in range(1, n):
    print(' ' * (n-i) + '*' * (2 * i -1))
for i in range(n,0,-1):
    print(' ' * (n-i) + '*' * (2 * i -1))