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

# 设置请求头
# header = {
#     'user-agent': 'imooc/v1'
# }
# res = requests.get('http://httpbin/ip', headers=header)


# 为请求设置请求超时时间
# res = requests.get('http://github.com', timeout=2)
# print(res.status_code)
# print(res.text)
# 请求超时的错误
# requests.exceptions.ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=7890): Read timed out. (read timeout=0.001)


# 获取cookies
# url = 'http://www.baidu.com'
# header = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }
# res = requests.get(url, headers=header)
# print(res.headers)
# print(res.text)
# print(res.cookies)
# print(res.cookies['H_PS_PSSID'])


# url = 'http://httpbin.org/cookies'
# # 使用dict构造cookies
# cookies = dict(cookies_are='hello imooc')
# res = requests.get(url, cookies=cookies)
# print(res.text)


