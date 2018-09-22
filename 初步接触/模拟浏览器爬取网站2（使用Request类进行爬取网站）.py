import urllib.request
url = "https://blog.csdn.net/"
req = urllib.request.Request(url)
#使用urllib.request.Request(url)
# 创建一个Request对象并赋给变量req，
req.add_header('
User-Agent',' Mozilla/5.0 (Windows NT 10.0;
Win64; x64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/64.0.3282.140 Safari/537.36
Edge/17.17134')
data = urllib.request.urlopen(red).read()
