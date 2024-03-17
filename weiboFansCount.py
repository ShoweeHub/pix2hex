import requests
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=7826543514'
req = requests.get(url)
print(req.json())
print(req.json()['data']['userInfo']['followers_count'])
