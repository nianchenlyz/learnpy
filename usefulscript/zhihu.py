'''���ߣ�����
���ӣ�https://www.zhihu.com/question/28975391/answer/100796070
��Դ��֪��
����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������'''

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
                print ('�����˵�'+str(i)+u'��ͼƬ')
                i+=1
                sleep(random.uniform(0.5,1))
            except:
                print ('ץ©1��')
                pass
        sleep(random.uniform(0.5,1))
        
if __name__=='__main__':
    main()     
