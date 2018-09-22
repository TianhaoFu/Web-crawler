import urllib.request
keywd="hello"
url="http://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
#爬去网页中的数据并保存再一个变量当中
fhandle=open("E:\python学习\爬虫\初步接触")
fhandle.write(data)
fhandle.close()
#导入本地
