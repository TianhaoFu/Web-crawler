import urllib.request
file = urllib.request.urlopen("http://www.baidu.com")
data = file.read()
dataline = file.readline()
print(dataline)
#爬取一个网页并将爬取到的内容读取出来付给一个变量
fhandle = open("D:/python6/myweb/part4/1.html","wb")
fhandle.write(data)