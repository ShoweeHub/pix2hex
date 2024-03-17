import requests

url = 'https://weatherapi.market.xiaomi.com/wtr-v3/weather/current'
params = {
    'locationKey': 'weathercn:101130101',
    'appKey': 'weather20151024',
    'sign': 'zUFJoAR2ZVrDy1vF3D07',
    'isGlobal': False,
    'locale': 'zh_cn'
}
req = requests.get(url, params=params)
print(req.url)
print(req.status_code)
print(req.json())
print(req.json()['temperature'])
print(req.json()['humidity'])
