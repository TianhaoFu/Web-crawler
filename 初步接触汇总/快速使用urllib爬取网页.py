import urtlllib.request
file = urtllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readline()
fhandle=open("D:/Python35/myweb/part4/1.html","web")
#使用二进制写入的方式打开
fhandle.write(data)
fhandle.close()

