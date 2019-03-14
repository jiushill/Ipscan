#uthor:九世
#time:2019/3/13

import requests
import re
from bs4 import BeautifulSoup
import os


p=__import__('plugin.portscan',fromlist=True)
w=__import__('plugin.portscan',fromlist=True)
sd=__import__('plugin.shodan_search',fromlist=True)
portscan=getattr(p,'portscan')
cx=getattr(w,'jiancha')
searchs=getattr(sd,'search')

countrys=[]
number=[]
daihao=[]
zon={}
start=[]
stop=[]

def country():
    global rqt
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='http://ip.bczs.net/countrylist'
    try:
        rqt=requests.get(url=url,headers=headers)
    except Exception as r:
        print('[-] 你这网咋回事啊，小老弟')
        exit()

    zz=re.findall("<tr class='ip2'>.*</tr>",rqt.text)
    for r in zz:
        hr=BeautifulSoup(str(r),'html.parser')
        for h in hr.find_all('td'):
            pz=re.sub('<td><a href=".*" title=".*">.*</a></td>','',str(h))
            pz=re.sub('<td class="r"><a href="/country/.*" title=".*">.*</a></td>','',str(pz))
            zz=re.findall('<td>.*</td>',str(pz))
            if len(zz)==0:
                del zz
            try:
                for i in zz:
                    cs=re.findall('<td>[\u4e00-\u9fa5].*</td>',str(i))
                    if len(cs)!=0:
                        countrys.append(cs[0])
                    nr=re.findall('<td>[0-999].*</td>',str(i))
                    if len(nr)!=0:
                        number.append(nr[0])
                    dh=re.findall('<td>[A-Z].*</td>',str(i))
                    if len(dh)!=0:
                        daihao.append(dh[0])
            except:
                pass


def sc():
    country()
    for k in range(0, len(countrys)):
        print('序号:{}   国家:{}  国家代号:{}'.format(str(number[k]).replace('<td>','').replace('</td>',''),str(countrys[k]).replace('<td>','').replace('</td>',''),str(daihao[k]).replace('<td>','').replace('</td>','')))
        zon[str(countrys[k]).replace('<td>','').replace('</td>','')]=str(daihao[k]).replace('<td>','').replace('</td>','')



def iplist(data):
    print('[+] 抓取的国家是:{}'.format(data))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    urls='http://ip.bczs.net/country/{}'.format(data)
    try:
        rvq=requests.get(url=urls,headers=headers)
        zz=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)-',str(rvq.text))
        zp=re.findall('-(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',str(rvq.text))
        for s in zz:
            start.append(str(s).replace("'",'').replace(',','.').replace('(','').replace(')','').replace('. ','.'))
        for p in zp:
            stop.append(str(p).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
    except Exception as r:
        print('[-] 小老弟，砸回事啊:{}'.format(r))

    print('[+] 国家IP范围列表')

    for k in range(0,len(start)):
        print('[+] IP开始范围:{} IP结束范围:{}'.format(start[k],stop[k]))
        portscan(start[k],stop[k])

def fwrite(data,file):
    if data in zon.keys():
        data=zon[data]
    print('[+] 抓取的国家是:{}'.format(data))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    urls = 'http://ip.bczs.net/country/{}'.format(data)
    try:
        rvq = requests.get(url=urls, headers=headers)
        zz = re.findall(
            '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)-',
            str(rvq.text))
        zp = re.findall(
            '-(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',
            str(rvq.text))
        for s in zz:
            start.append(str(s).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
        for p in zp:
            stop.append(str(p).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
    except Exception as r:
        print('[-] 小老弟，砸回事啊:{}'.format(r))

    print('[+] 国家IP范围列表')
    for k in range(0, len(start)):
        print('[+] IP开始范围:{} IP结束范围:{}'.format(start[k], stop[k]))
        a = '[0-9]{1,}'
        zz = re.findall(a, start[k])
        zp = re.findall(a, stop[k])
        for i in range(int(zz[0]), int(zp[0]) + 1):
            for s in range(int(zz[1]), int(zp[1]) + 1):
                for u in range(int(zz[2]), int(zp[2]) + 1):
                    for q in range(int(zz[3]), int(zp[3]) + 1):
                        ip = '{}.{}.{}.{}'.format(i, s, u, q)
                        print(ip)
                        print(ip,file=open('file/{}'.format(file),'a',encoding='utf-8'))

    if os.path.exists('file/{}'.format(file)):
        print('[+] 文件:{}写入成功'.format(file))
    else:
        print('[-] 文件:{} 写入失败'.format(file))

def wzjc(data):
    if data in zon.keys():
        data=zon[data]
    print('[+] 抓取的国家是:{}'.format(data))
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    urls = 'http://ip.bczs.net/country/{}'.format(data)
    try:
        rvq = requests.get(url=urls, headers=headers)
        zz = re.findall(
            '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)-',
            str(rvq.text))
        zp = re.findall(
            '-(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',
            str(rvq.text))
        for s in zz:
            start.append(str(s).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
        for p in zp:
            stop.append(str(p).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
    except Exception as r:
        print('[-] 小老弟，砸回事啊:{}'.format(r))

    print('[+] 国家IP范围列表')

    for k in range(0, len(start)):
        print('[+] IP开始范围:{} IP结束范围:{}'.format(start[k], stop[k]))
        cx(start[k],stop[k])

def iplist_start():
    sc()
    user=input('输入国家名称:')
    if user in zon.keys():
        iplist(zon[user])

def search(data):
        if data in zon.keys():
            data = zon[data]
        print('[+] 抓取的国家是:{}'.format(data))
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
        urls = 'http://ip.bczs.net/country/{}'.format(data)
        try:
            rvq = requests.get(url=urls, headers=headers)
            zz = re.findall(
                '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)-',
                str(rvq.text))
            zp = re.findall(
                '-(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',
                str(rvq.text))
            for s in zz:
                start.append(
                    str(s).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
            for p in zp:
                stop.append(
                    str(p).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').replace('. ', '.'))
        except Exception as r:
            print('[-] 小老弟，砸回事啊:{}'.format(r))

        print('[+] 国家IP范围列表')
        for k in range(0, len(start)):
            print('[+] IP开始范围:{} IP结束范围:{}'.format(start[k], stop[k]))
            a = '[0-9]{1,}'
            zz = re.findall(a, start[k])
            zp = re.findall(a, stop[k])
            for i in range(int(zz[0]), int(zp[0]) + 1):
                for s in range(int(zz[1]), int(zp[1]) + 1):
                    for u in range(int(zz[2]), int(zp[2]) + 1):
                        for q in range(int(zz[3]), int(zp[3]) + 1):
                            ip = '{}.{}.{}.{}'.format(i, s, u, q)
                            searchs(ip)