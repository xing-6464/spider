import re

pattern = re.compile(r'\d+')

# match
# match是头部位置开始匹配
# m1 = pattern.match('one12twothree34four')
# print(m1) # None

# m2 = pattern.match('one12twothree34four', 3, 10)
# # group查看匹配结果
# print(m2.group())

# search 是字符串任意位置开始匹配
# m1 = pattern.search('one12twothree34four')
# print(m1)

