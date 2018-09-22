import re
import urllib.request
def getlink(url):
    headers = ("User-Agent")
    opener = urllib.request.build_opener()
    opener.add.headers = [headers]
    urllib.install.intall_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    pat = '(http？://[^\s)";]+\.(\w|/)*'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link
url = "http://blog.csdn.net/"
linklist = getlink(url)
for link in linklist:
    print(link[0])