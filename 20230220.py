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