'''作者：挖数
链接：https://www.zhihu.com/question/28975391/answer/100796070
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''

import requests
import urllib
import re
import random
from time import sleep

def main():
    url='xxx'
    headers={xxx}
    i=925
    for x in xrange(1020,2000,20):
        data={'start':'1000',
    'offset':str(x),
    '_xsrf':'a128464ef225a69348cef94c38f4e428'}
        content=requests.post(url,headers=headers,data=data,timeout=10).text
        imgs=re.findall('<img src=\\\\\"(.*?)_m.jpg',content)    
        for img in imgs:
            try:
                img=img.replace('\\','')
                pic=img+'.jpg'
                path='d:\\bs4\\zhihu\\jpg4\\'+str(i)+'.jpg'
                urllib.urlretrieve(pic,path)
                print ('下载了第'+str(i)+u'张图片')
                i+=1
                sleep(random.uniform(0.5,1))
            except:
                print ('抓漏1张')
                pass
        sleep(random.uniform(0.5,1))
        
if __name__=='__main__':
    main()     
