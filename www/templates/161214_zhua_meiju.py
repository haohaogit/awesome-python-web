import sys
import re
import requests
import os
import time
import threading
from bs4 import BeautifulSoup
from Download import download

#sys.s
class zhua_meiju(download):
    headers = { 'User-Agent': "Mozilla/5.0 (windows NT 6.1; WOW64) AppleWebkit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    def get_url(self):
        try:
            for n in range(23793, 25000):
                start_url = 'http://cn163.net/archives/'
                url = start_url + str(n) + '/'
                print(url)
                if download.get(self,url,3).status_code==404:
                    continue
                else:
                    print('123')
                    self.save_link(url)
        except:
            pass
    def save_link(self,url):
        print('abc')
        try:
            # content = requests.get(url, headers=self.headers, timeout=3)
            # print(content.text)
            data=download.get(self,url,3)
            content=data.text

            Soup = BeautifulSoup(content, 'lxml')
            all_strong = Soup.find('div', class_='entry').find_all('strong')
            print(all_strong)


            # 利用keyword参数也可以准确找到特定的url （href;text ）
            # 例1
            # soup.find_all(href=re.compile("elsie"), id='link1')
            # # [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
            # 例2
            # soup.find_all("a", class_="sister")
            # # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
            # #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
            # #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
            # 例3   实践
            # Soup = BeautifulSoup(content, 'lxml')
            # all_strong = Soup.find('div', class_='entry').find_all('strong')
            # print(all_strong)
            # # all_url=Soup.find_all(href=re.compile("%E6%91%A9%E7%99%BB%E5%AE%B6%E5%BA%AD"))
            # all_url = Soup.find_all(href=re.compile("1024X576"))
            # for ul in all_url:
            #     print(ul['href'])


            name_pattern=re.compile(r'<h2 class="entry_title">(.*?)</h2>',re.S)
            zimu_pattern=re.compile(r'')
            link_pattern='"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'
            ju_name=re.findall(name_pattern,content)
            print(ju_name)
            ji_link =set(re.findall(link_pattern,content))
            link_dict={}
            count1=len(ji_link)
        except :
            pass
        for i in ji_link:
            link_dict[int(i[1][1:3])*100+int(i[2][1:3])]=i   #把剧集按s和e 提取编号
        try:
            with open(ju_name[0].replace('/','')+'.txt','w') as f:
                print(ju_name[0])
                for i in sorted(list(link_dict.keys())):  # 按季数+集数排序顺序写入

                    f.write(link_dict[i][1]+': '+link_dict[i][0] + '\n')
                print("Get links ... ",ju_name[0],count1)
        except :
            pass
    def main(self):
        isExists = os.path.exists(os.path.join("E:\mzitu", 'meiju'))
        if not isExists:
            print(u'建了一个名字叫做 meiju 的文件夹')
            os.makedirs(os.path.join("E:\mzitu", 'meiju'))  # 创建一个存放套图的文件夹
            os.chdir("E:\mzitu\\" + 'meiju')
        else:
            print(u'名字叫做 meiju 的文件夹已经纯在了')
            os.chdir("E:\mzitu\\" + 'meiju')
        # os.makedirs(os.path.join("E:\mzitu", 'meiju'))  # 创建一个存放套图的文件夹
        # os.chdir("E:\mzitu\\" + 'meiju')
        self.get_url()
        #thread1 = threading.Thread(target=self.get_urls())
        #thread1.start()
        #thread1.join()


if __name__ == '__main__':
    start = time.time()
    a = zhua_meiju()
    a.main()
    end = time.time()
    print(end ,'-', start)
