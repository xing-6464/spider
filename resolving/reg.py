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


# findall 搜索全文匹配符合的字符串返回list
# m1 = pattern.findall('one12twothree34four')
# print(m1)

