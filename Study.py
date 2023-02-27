# 1-1 나누어 입력받기
a,b  = map(int, input().split())

# 1-2. 입력 출력 가속
import sys 
N = int(sys.stdin.readline())
sys.stdout.write(str(N))

# 2-1. 우아한 배열 입력
Map = [list(map(int, input().split())) for _ in range(int(input()))]

# 2-2. 정수와 배열이 같은 줄에 들어오는 경우
N, *arr = map(int, input().split())

# 3-1. 배열을 연결해서 출력 1
arr = [1, 2, 3, 4]
print(''.join(map(str, arr))) # map 함수를 이용하여 sring 형식

# 3-2. 배열을 연결해서 출력 2
arr = [1, 2, 3, 4]
print(*arr) # [] , 를 뺴고 출력


# 1-1. 최대, 최소
import sys
ans = sys.maxsize # ans 값을 출력하면 큰 값이 출력, ans += 1 가능

# 2-1. 10진수 → 2, 8, 16진수 변환
bin(42); oct(42); hex(42)

# 2-2. 2, 8, 16진수 → 10진수 변환
int('0o74', 8)

# 3-1. 문자열을 거꾸로
apph = "ABCD"
apph[::-1]

# 4-1. 배열 초기화
N, M = map(int, input().split())
arr = [[0] * N for _ in range(M)] # 가로 세로

# 4-3. 배열 원소 갯수
list.count(3)

# 4-5. 배열 정렬

arr.sort(key=lambda x:(x[0], x[1]))
