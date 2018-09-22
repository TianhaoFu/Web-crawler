import urllib.request
url = "httr://www.baidu.com/s?wd="
key="韦唯老师"
key_code = urllib.request.quote(key)
url_all = url+kry_code
#转换编码
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req)
#爬取网站数据
fh=open("D:/Python35/myweb.part4/5.html","wb")
fh.write(data)
fh.close()
"""构建相应的URL网址，URL转化为Request模式，打开url，读取数据，打开本地文件夹，保存数据，关闭文件夹"""

