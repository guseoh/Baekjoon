# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# if a > b:
#     print(a)
# else: print(b)

# words = input().upper() # zZa => ZZA
# ww = list(set(words)) # 중복 제거 -> ZA

# cnt = []
# for i in ww:
#     count = words.count(i) # 2 1
#     cnt.append(count) # [2, 1]

# if cnt.count(max(cnt)) > 1:
#     print('?')
# else:
#     max1 = cnt.index(max(cnt)) # count 숫자 최대값 인덱스
#     print(ww[max1])

# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append

# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])

def GCD(a,b): # 유클리드 호제법
    if b % a: 
        return GCD(b % a, a)
    else: return a
    
n,m = map(int, input().split(':'))
a = GCD(n,m)
print(n // a, end='')
print(':', end='')
print(m // a, end='')