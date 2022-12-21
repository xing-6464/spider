import requests


for i in range(1, 5):
    url = 'http://yushu.talelin.com/book/search?q=python&page={}'.format(i)
    res = requests.get(url)

    html_file_name = 'page_{}.html'.format(i)
    with open(html_file_name, 'w', encoding='utf-8') as f:
        f.write(res.text)
    print('网页html已经下载完毕')
