import urllib.request
import bs4 as bs
import requests
import re
import time
import random

def parser(page):
    urls = []
    for i in range(2000,page):
        url = 'http://jandan.net/ooxx/page-{}'.format(str(i))
        urls.append(url)
    for a in urls:
        sauce = urllib.request.urlopen(a)
        soup = bs.BeautifulSoup(sauce,'lxml')
        imgs = soup.find_all('img')
        for img in imgs:
            src = re.compile('src="//(.*)".*/>')
            findsrc = re.findall(src,str(img))
            try:
                for i in findsrc:
                    time.sleep(0.05)
                    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
                    req = urllib.request.Request(url='https://'+i, headers=headers)
                    data = urllib.request.urlopen(req).read()
                    path = 'images/'+str(random.randint(1,10000))+'.jpg'
                    with open(path,'wb') as f:
                        f.write(data)
            except urllib.error.URLError as e:
                print('except:', '有张图片失效了')
            finally:
                print('图片正在生成')

if __name__ == '__main__':
    parser(2323)
