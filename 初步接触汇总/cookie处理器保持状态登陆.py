import urllib.request
import urllib.parse
import http.cookiejar
url = "https://qzonestyle.gtimg.cn/qzone/qzactStatics/configSystem/data/576/config1.js"
postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header('Uesr-Agent','Mozilla/5.0 (windows NT)')
cjar = http.cookiejar.CookieJar()
#创建对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建openern对象
urllib.request.install)opener(opener)
#将openern安装为全局
data = urllib.request.urloprn(rep).read()
fhandle = open("E:\python学习\爬虫\爬取的数据","wb")
fhandle.write(data)
fhandle.close()
url2 = "https://user.qzone.qq.com/2074934525"
req2 = urllib.request.Request(url2,postdata)
req.addheader('Uesr-Agent','Mozilla/5.0 (windows NT)')
data = urllib.request.urlopen(req2).read()
fhandle = open("E:\python学习\爬虫\爬取的数据","wb")
fhandle.write(data)
fhandle.close()
