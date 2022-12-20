import requests

# url = 'http://httpbin.org/'

# # get请求
# response = requests.get(url + 'ip')
# print(response.text)

# # post请求
# data = {'name': 'imooc'}
# res = requests.post(url + 'post', data=data)
# print(res.text)

# 代参数的get请求
# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
# res = requests.get('http://httpbin.org/get', params=data)
# print(res.url)
# print(res.headers)

# 使用get请求获取图片数据
# res = requests.get('https://www.imooc.com/static/img/index/logo2020.png')
# with open('imooc.png', 'wb') as f:
#     f.write(res.content)

# 请求json数据
# res = requests.get('http://httpbin.org/ip')
# data = res.json()
# print(data)
# print(data['origin'])
