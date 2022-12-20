import requests

url = 'http://httpbin.org/'

# get请求
response = requests.get(url + 'ip')
print(response.text)

# post请求
data = {'name': 'imooc'}
res = requests.post(url + 'post', data=data)
print(res.text)
