#author:九世
#time:2019/3/13

import socket
import configparser
import re
import threading
import requests

port=[]
threads=0
timeout=0

locak=threading.BoundedSemaphore(100)

def read():
    global threads,timeout
    dk=configparser.ConfigParser()
    dk.read('config/config.txt')
    pt=dk.get('scan','port')
    pz=re.findall('[0-9]{1,}',pt)
    threads+=int(dk.get('scan','thread'))
    timeout+=int(dk.get('scan','timeout'))
    for p in pz:
        port.append(p)



read()

def scan(host,port):
    sock=socket.socket()
    try:
        sock.connect((host,int(port)))
        print('{}:{}/open'.format(host,port))
        print('{}:{}/open'.format(host, port),file=open('file/portscan.txt','a',encoding='utf-8'))
    except:
        pass

def jc(ip):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url = 'http://www.26595.com/tool/sameip/?action=sed'
    data = {'cx_33': '{}'.format(ip), 'action': '(unable to decode value)'}
    rqt = requests.post(url=url, headers=headers, data=data)
    zz = re.findall('.*</span>&nbsp;', rqt.text)
    if len(zz) > 0:
        print('[+] 查询到IP:{}下的网站'.format(ip))
        for z in zz:
            print(str(z).lstrip().replace('</span>&nbsp;', ''))
            print(str(z).lstrip().replace('</span>&nbsp;', ''),
                  file=open('file/{}.txt'.format(ip), 'a', encoding='utf-8'))
    else:
        print('[-] IP:{}没有查询到网站'.format(ip))

def jiancha(start_host,stop_host):
    a = '[0-9]{1,}'
    zz = re.findall(a, start_host)
    zp = re.findall(a, stop_host)
    for i in range(int(zz[0]), int(zp[0]) + 1):
        for s in range(int(zz[1]), int(zp[1]) + 1):
            for u in range(int(zz[2]), int(zp[2]) + 1):
                for q in range(int(zz[3])+1, int(zp[3]) + 1):
                    try:
                        ip = '{}.{}.{}.{}'.format(i, s, u, q)
                        jc(ip)
                    except:
                        pass

def portscan(start_host,stop_host):
    print('[+] 要爬的端口:{}'.format(port))
    print('[+] 扫描线程:{}'.format(threads))
    print('[+] 超时设置:{}'.format(timeout))
    a = '[0-9]{1,}'
    zz = re.findall(a, start_host)
    zp = re.findall(a, stop_host)
    for i in range(int(zz[0]), int(zp[0]) + 1):
        for s in range(int(zz[1]), int(zp[1]) + 1):
            for u in range(int(zz[2]), int(zp[2]) + 1):
                for q in range(int(zz[3]), int(zp[3]) + 1):
                    ip = '{}.{}.{}.{}'.format(i, s, u, q)
                    for j in port:
                        t=threading.Thread(target=scan,args=(ip,j))
                        t.start()

    locak.acquire()