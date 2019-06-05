import requests
from lxml import etree
import MySQLdb
import json

#       1. IP数据源
# 		2. 检测可用性
# 		3. 入库存储
# 		4. 对外提供获取IP接口
# 		5. 出库
# 		6. 原则上：出库的IP应该丢弃
# 			修改状态值
# 		7. 定期检查所有入库的IP的可用性

class IpProxiesPool(object):
    def __init__(self,maxsize=10,limit=3): # 最大值应该大于阈值
        # 测试用的网址
        self.testUrl='http://httpbin.org/ip'
        # 最大值
        self.max=maxsize
        # 阈值
        self.limit=limit
        # 创建解析时使用的列表
        self.l=[]
        # 设置页码
        self.n=1
        # 设置本机ip
        self.localIP=requests.get(self.testUrl).text  # 返回json串
        # 字符串--str
        # json串--- str
        self.initDB()

    def parseIP(self):
        pass
    # 5. 对外提供一个IP
    def getOneIP(self):
        self.cursor.execute(self.selectSQL)
        proxy=json.loads(self.cursor.fetchone()[0])
        # 标记已用IP
        self.cursor.execute(self.updateSQL,[proxy])
        self.conn.commit()


        self.autoAddIP()
        return proxy

    # 自动补货方法
    def autoAddIP(self):
        # 判断是否达到阈值
        if self.getCount()<=self.limit:
            # 刷新一次数据库
            self.regularValidate()
            # 加满
            self.provideIP()

    # 1. 对内提供IP数据源
    def provideIP(self,url='https://www.xicidaili.com/nn/'):
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        # 到达最大值
        while self.getCount()<self.max:
            datas = etree.HTML(requests.get(url + str(self.n), headers=headers).text)
            trs = datas.xpath('//tr')[1:]
            for i in trs:
                self.ip, self.port, self.types = i.xpath('.//td[2]/text() | .//td[3]/text() |.//td[6]/text()')
                proxy = {self.types: self.ip + ':' + self.port}
                # 验证是否可用
                if self.validateIP(proxy):
                    # 可用 入库
                    self.saveOneIP(proxy)
            if self.n>2000:
                self.n=1
            else:
                self.n+=1
            self.regularValidate()

    # 设置数据库初始化方法
    def initDB(self):
        # 设置数据库
        self.conn = MySQLdb.Connection(host='localhost', port=3306, user='root', password='123456', db='crawler',
                                       charset='utf8')
        self.cursor = self.conn.cursor()
        self.insertSQL='insert into proxies(proxy,status) values(%s,%s)'
        self.countSQL='select status from proxies where status=0'
        self.selectSQL='select proxy from proxies where status=0 limit 0,1'
        self.updateSQL='update proxies set status=1 where proxy=%s'
    # 3. 入库
    def saveOneIP(self,proxy):
        self.cursor.execute(self.insertSQL,[str(proxy),0]) # 0:可用
        self.conn.commit()

    # 2. 验证IP
    def validateIP(self,proxy):
        if self.localIP==requests.get(self.testUrl,proxies=proxy).text:
            # 失败--丢弃
            return False
        else:
            return True

    # 4. 查看数据库中可用IP的总数
    def getCount(self):
        return self.cursor.execute(self.countSQL)

    def regularValidate(self):
        for i in self.getAllIPs():
            if self.validateIP(i):
                # 可用
                self.cursor.execute('update proxies set status=0 where proxy='+str(i))
                self.conn.commit()


    def getAllIPs(self):
        self.cursor.execute('select proxy from proxies')
        for j in [i[0] for i in self.cursor.fetchall()]:
            # j: 每一个proxy
            yield json.loads(j)

if __name__ == '__main__':
    a=IpProxiesPool()
    a.provideIP()  # 1. 自动补满了IP  2. 如果小于阈值，自动补货 3. 根据情况自动刷新数据库，筛选出可用IP（包括新的和旧的）

