# a = input()
# aa = list(map(int, input().split()))
# aaa = max(aa)
# sum = sum(aa)
# print(sum * 100 / aaa / int(a))

text = input()  # count로 개수 세기
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(alphabet)):
    print(text.count(alphabet[i]), end=' ')