import urllib.request

data = dict()

data['tid'] = 'UA-128971539-1'
data['cid'] = '555'
data['t'] = 'event'
data['ec'] = 'video'
data['ea'] = 'play'
data['el'] = 'holiday'
data['ev'] = '300'

url = 'http://www.google-analytics.com/?'
for key, value in data.items():
    url += key + "=" + value + "&"

print(url)

urllib.request.Request(url, None)
