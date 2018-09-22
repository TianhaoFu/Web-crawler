import urllib.request
url1 = "https://www.csdn.net/"
headers = ("User-Agent","
   Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
64.0.3282.140 Safari/537.36 Edge/17.17134")
opener = urllib.request.build_opener()
#创建自定义的urllib.request.build_opener对象
opener.addheaders = [headers]
#使用open方法打开对应的网址
#此时，打开操作是已经具有头信息的打开操作行为
#即模仿为浏览器去打开
data = opener.open(url).read().decode()
fhandle = open("E:\python学习\爬虫\初步接触","wb")
fhandle.write(data)
