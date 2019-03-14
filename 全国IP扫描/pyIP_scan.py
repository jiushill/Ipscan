#author:九世
#time:2019/3/13

z=__import__('plugin.zhua',fromlist=True)
h=__import__('plugin.zhua',fromlist=True)
s=__import__('plugin.zhua',fromlist=True)
w=__import__('plugin.zhua',fromlist=True)
iplist_start=getattr(z,'iplist_start')
huoqus=getattr(h,'fwrite')
sc=getattr(s,'sc')
wps=getattr(w,'wzjc')
zb=getattr(z,'search')


class qg:
    def  banner(self):
        b="""
        
.-.                               
: :                               
: :.---.  .--.  .--.  .--.  ,-.,-.
: :: .; ``._-.''  ..'' .; ; : ,. :
:_;: ._.'`.__.'`.__.'`.__,_;:_;:_;
   : :                            
   :_;                            
        """
        print(b)
    def huoqu(self):
        sc()
        d=input('请输入国家:')
        f=input('请输入要保存的文件名:')
        huoqus(d,f)
    def zhuas(self):
        iplist_start()
    def wp(self):
        sc()
        d=input('请输入国家:')
        wps(d)
    def shodan(self):
        sc()
        d=input('请输入国家:')
        host=zb(d)

if __name__ == '__main__':
    ojbk=qg()
    ojbk.banner()
    print('')
    print('1.获取指定国家的IP范围(并写入txt)')
    print('2.扫描指定国家的IP范围')
    print('3.检测指定国家的IP范围里是否有网站')
    print('4.shodan搜索IP')
    jg={'1':ojbk.huoqu,'2':ojbk.zhuas,'3':ojbk.wp,'4':ojbk.shodan}
    user=input('请选择:')
    if user in jg:
        jg[user]()
