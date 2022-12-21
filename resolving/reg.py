import re

pattern = re.compile(r'\d+')

# match
# match是头部匹配
m1 = pattern.match('one12twothree34four')
print(m1) # None

m2 = pattern.match('one12twothree34four', 3, 10)
# group查看匹配结果
print(m2.group())


