import re
import urllib.request
def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    #url局部变量
    html1 =str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?)\.jpg">'
    x=1
    for imageurl in imaglist:
        imagename = "E:\python学习\爬虫\爬取的数据"
        imageurl = "http://" + imageurl1
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x +=1

        x+=1
    for i in range(1,79):
        url = "" +str(i)
        craw(url,i)
        
