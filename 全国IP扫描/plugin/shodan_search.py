#author:九世
#time:2019/3/14

import shodan
import configparser

conf=configparser.ConfigParser()
conf.read('config/config.txt')
key=conf.get('scan','shodan_key')

def search(host):
    print('[+] IP:{}搜索结果'.format(host))
    print('[+] IP:{}搜索结果'.format(host),file=open('file/shodan_search.txt','a',encoding='utf-8'))
    api=shodan.Shodan(key)
    try:
        result=api.search('{}'.format(host))
        print('='*50)
        if len(result['matches'])>0:
            for r in result['matches']:
                for c in r.items():
                    print('{}:{}'.format(c[0],c[1]))
                    print('{}:{}'.format(c[0], c[1]),file=open('file/shodan_search.txt','a',encoding='utf-8'))
                    print('')
        else:
            print('[-] 未能从shodan中找到对应的数据')

    except:
        pass
