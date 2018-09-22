import urllib.request
import urllib.parse
url = "http://www.iqianyue.com/mypost"
postdata = urllib.parse.urlencode({
    "name":"ceo@iqianyue.com"
    "pass":"aA123456"
}).encode('utf-8')
#按照utf-8的方式进行编码
#建立需要通过表单传递的数据变量并予以赋值
req= urllib.request.Request(url,postdata)
req.add_header()
data=urlllib.request.urlopen(req).read()
#模拟浏览器进行爬取
fhandle=open("E:\python学习\爬虫\初步接触")
fhandle.write(data)
fhandle.close()
#将爬取的数据进行储存
