import re
a = []
sum = 0
ss = "abc1adad2"
num = re.sub(r'[^0-9]','',ss)
for i in num:
    sum += int(i)

print(sum)