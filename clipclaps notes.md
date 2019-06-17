# outline

> > ```ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpOR3RwWlJpczFWc0Y=@35.238.99.50:33866/?outline=1```



# My Google:

> > ```账号：deerking321@gmail.com```
> >
> > ```密码：zp920316```

# news API

> >```markdown
> >deerking007   16601348816@163.com  
> >BBC  api_key='cb7a4ae15a98429890aeedb9a7b460a0'
> >
> >zhangpeng     zhangpeng@clipclaps.com
> >ABC    e7d5104fc5c74e259dbe2427b68257fb
> >```

# 部署到服务器

> > #### 测试和正式服务
> >
> > ```markdown
> > >>test 
> > 		http://console.cc.test.clipclaps.tv/crawler/product/list?auditStatus=0&pageNum=0&pageSize=50&type=5
> > 		http://console.cc.test.clipclaps.tv/
> > >>formal
> > 		http://console.cc.clipclaps.tv/crawler/product/list?auditStatus=0&pageNum=0&pageSize=50&type=5
> > 		http://console.cc.clipclaps.tv/
> > ```
> >
> > 查看ssh历史
> >
> > history | grep ssh
> >
> > ####登陆跳板机：
> >
> > ssh -i usEast01-sshkey-devuser.pem devuser@<54.204.52.128>
> >
> > ####然后进入爬虫服务器：
> >
> > ssh 10.1.15.11     test
> >
> > ssh 10.1.15.172     formal
> >
> > 上传文件先由本地上传到跳板机
> >
> > scp -i usEast01-sshkey-devuser.pem /Users/zp/Desktop/news/saveSqldb.py devuser@54.204.52.128:/home/devuser
> >
> > 上传到服务器
> >
> > scp topbuzz.py devuser@10.1.15.11:/app/crawler/project/news
> >
> > 执行python环境
> >
> > ####启用python3.7环境执行命令 **
> >
> > . pyth3 或 source pyth3
> >
> > export PYTHONPATH=~/.local/lib/python3.7/site-packages
> >
> > virtualenv .
> >
> > 取消python3.7环境执行命令
> >
> > nopyth3
> >
> > telnet localhost 30008
> >
> > telnet 127.0.0.1 30008
> >
> > 测试POST入库：
> >
> > <http://localhost/crawler/article/transfer?type=1&source=1&title=1&content=21312131313131313>
> >
> > curl <http://127.0.0.1:30006/crawler/article/transfer> -d 'source=1&title=11123131312just%20do%20it&content=sdssdsdsdsdsdsdsdds'
> >
> > ```正则匹配键值对:"\"param\":\\{([^\\}]*)\\}"```



#Source

> > ### ```SmartNews     Source:5```

> > ### ```FlipBoard     Source:6```

> > ### ```TopBuzz       Source:1```

> > ### ```NewsBreak     Source:2```

> > ### ```BuzzFeed      Source:3```

> > ### ```GoogleNews    Source:4```



# 修改Terminal  >  fish

> > ``` you can use `chsh` to set default shell to `/usr/local/bin/fish```

> > 进入Terminal直接是fish界面

> > **```配置环境: vi ~/.config/fish/config.fish```**

> > ```vi ~/.bash_profile```

# Terminal工具

> >> **tig让git命令行可视化**
> >>
> >> ```brew install tig tree ag fzf```
> >
> >> **工具**
> >>
> >> ```brew install neovim```
> >
> >> **Terminal工具**
> >>
> >> `brew install tmux`
> >
> >> `brew install coreutils reattach-to-user-namespace axel git-extras fswatch mmv expect yarn`
> >
> >> ```sudo 超级用户```
> >
> >> ls -l 查看权限
> >>
> >> 赋值权限 sudo chown -R mr.zhang:staff wpsoffice.app/

# python3安装与卸载

## 安装

```markdown
>>> mac Terminal    brew install python
```

## 卸载

```markdown
>>> mac Terminal   
1.删除Python 3.X frameworksudo 
rm -rf /Library/Frameworks/Python.framework/Versions/3.6
2.删除Python 3.6 应用目录
sudo rm -rf “/Applications/Python 3.6”
3.删除/usr/local/bin 目录下指向的Python3.6的连接
cd /usr/local/bin/ 
ls -l /usr/local/bin | grep ‘/Library/Frameworks/Python.framework/Versions/3.6’  brew prune 
4.Python3.6的信息配置在 ~/.bash_profile 文件中，将其相关信息删除

```

# 2019.5.8

分析寻找新源





# 2019.5.7

**对buzzfeed 进行解析，段落文本内容利用lxml进行解析，buzzfeed 解析文本存在超链接不能爬取，造成文章爬取不完整，对topbuzz wb进行解析，顺利入库。**

```python
import requests, time, json, uuid, random
from lxml import etree
import urllib.request
import urllib.parse


class TopBuzz_news(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.   36'}
        self.cookies = {'cookies': 'odin_tt=25f29c3c11ab624e32ea123b341f8e8ad3b9254cb1bcb00828ea8bbdf642ee3018a6a10f8ce2d4c3bb22af93a7fbcf4f44f76469931ce1241c8907041d196a1c; tt_webid=6675470162378032646; __tea_sdk__user_unique_id=6675470162378032646; __tea_sdk__ssid=f4cef532-3e68-4425-a4fa-8963bda2fdc3; csrf-token=da1ad8433b7acb6730721e47b072bc7ec710c4e3; csrf-secret=QBi0atkMP4iR2oosQVsHoAxAo7LA2Qzm'}
        self.keyword = ['foryou','entertainment','sports','lifestyle','gaming','food','tech','autos']
        self.t = time.time()
        self.filter_url = 'http://console.cc.clipclaps.tv/crawler/log'
        self.post_url = 'http://127.0.0.1:30008/crawler/article/transfer'
        self.downloadPath = '/data/crawler'
        self.picPath = '/topbuzz/picture/'


    def run(self):
        for cls in self.keyword:
            print('cls:\t', cls)
            url = 'https://www.topbuzz.com/pgc/feed?content_space=bd&language=en&region=us&user_id=6675470162378032646' \
                  '&channel_name=' + cls + \
                  '&classification=all' \
                  '&max_behot_time=' + str(self.t)
            self.parsing_topBuzz_list_page(list_url=url)
            time.sleep(random.uniform(60, 70))


    def parsing_topBuzz_list_page(self, list_url):
        res = requests.get(url=list_url, headers=self.headers, cookies=self.cookies).text
        data = json.loads(res)
        item = data['data']['feed']['items']
        # 分析列表页，获得详情页url
        for i in range(len(item)):
            group_id = item[i]['group_id']
            impr_id = item[i]['impr_id']
            user_id = item[i]['author_info']['user_id']
            detail_url = 'https://www.topbuzz.com/a/' \
                         + group_id + \
                         '?app_id=1106' \
                         '&gid=' + group_id + \
                         '&impr_id=' + impr_id + \
                         '&language=en' \
                         '&region=us' \
                         '&user_id=' + user_id + \
                         '&c=sys'
            filter_data = self.filter_data(details_url=detail_url)
            if filter_data == '数据已存在':
                print('数据已存在')
            else:
                self.parsing_details_page(details_url=detail_url)


    def parsing_details_page(self, details_url):
        time.sleep(random.uniform(5, 10))
        result = requests.get(url=details_url, headers=self.headers, cookies=self.cookies).text
        html = etree.HTML(result)
        jobId = time.time()
        sourceUrl = details_url
        title = ''.join(html.xpath('//div[@class="title"]/text()'))
        authorName = ''.join(html.xpath('//div[@class="name active"]/text()'))
        releaseTime = ''.join(html.xpath('//div[@class="publishTime"]/text()'))
        content_list = html.xpath('//div[@class="editor-container"]//p/text()')
        content = '<p>'.join([i.replace("\n", '').strip() for i in content_list]).replace("<p><p>", '<p>')
        img = self.download_img(html=html)
        if img is None or img == '' or content is None or content == '':
            pass
        else:
            data = {'jobId': int(jobId), 'sourceUrl': sourceUrl, 'title': title, 'authorName':authorName,
                    'releaseTime': releaseTime, 'content': content, 'img': img}
            print('data:\n', data)
            self.save_data(data=data)


    def download_img(self, html):
        try:
            pic_url_list = html.xpath('//img[@class="image"]//@src')
            img_id = str(uuid.uuid4()).replace('-','')
            index = 1
            img_list = []
            if pic_url_list == []:
                pass
            else:
                for pic_url in pic_url_list:
                    urllib.request.urlretrieve('https:' + pic_url, r'%s.jpg' % (self.downloadPath + self.picPath + str(img_id) + "-" + str(index)))
                    img_list.append(r'%s.jpg' % (self.picPath + str(img_id) + "-" + str(index)))
                    index += 1
                img = ','.join(img_list)
                return img
        except:
            pass


    def filter_data(self ,details_url):
        data1 = urllib.parse.urlencode({
            'type': int(5),
            'days': int(3),
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.filter_url, data=data2)
        status = re.read().decode('utf-8')
        result = json.loads(status)
        data = result['data']
        data_list = []
        for kw in data:
            data_list.append(data[kw])
        if details_url in data_list:
            return '数据已存在'
        else:
            return details_url


    def save_data(self, data):
        data1 = urllib.parse.urlencode({
            'source': 1,
            'jobId': data['jobId'],
            'sourceUrl': data['sourceUrl'],
            'title': data['title'],
            'authorName': data['authorName'],
            'releaseTime': data['releaseTime'],
            'content': data['content'],
            'img': data['img'],
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.post_url, data=data2)
        status = re.read().decode('utf-8')
        print('status:\n', status)

if __name__ == '__main__':
    tb = TopBuzz_news()
    tb.run()
```





# 2019.5.6

**今天对 abc news 进行解析，通过研究发现newspaper model 的	fulltext可以直接利用 request.get()解析的HTML页面解析文本段落，优化了解析过程，节约了资源**

```python
from newsapi import NewsApiClient
import time, requests, random, json, uuid
from lxml import etree
import urllib.parse
import urllib.request
from newspaper import fulltext



class ABC_News(object):
    def __init__(self):
        self.news_api = NewsApiClient(api_key='e7d5104fc5c74e259dbe2427b68257fb')
        self.key_word = ['News','International','U.S.','Lifestyle', 'Technology', 'Entertainment', 'Sports', 'Health']
        self.t = time.time()
        self.point_time = time.strftime('%Y-%m-%d', time.localtime(self.t))
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        self.cookies = {'cookie': 'cookieMonster=1; _cb_ls=1; SWID=522fc1e1-4ffd-4802-86fa-d7475f8dca57; optimizelyEndUserId=oeu1557122779744r0.05588715173473946; s_vi=[CS]v1|2E67E7728507B2CE-4000011580009D3A[CE]; __gads=ID=b52dc242d5ad893e:T=1557122797:S=ALNI_MaWnnuLLKP88qrPEsPEVuViaoGlJg; UNID=0df479d5-1639-4404-b6a8-36d731a7876d; UNID=0df479d5-1639-4404-b6a8-36d731a7876d; _cb=Dz5K21B0CX5JDkjMG; _v__chartbeat3=DbUUrKDDGTaEDqauaQ; _cb_svref=null; AkamaiAnalytics_BrowserSessionId=4d41ba72-5ab2-8f33-46aa-f5748aca9647; HTML_VisitIntervalStartTime=1557125661015; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B; adnum=3undefined; _chartbeat2=.1557122809880.1557125676423.1.DoKBmGC2OW5QDWek5PEERi8oZtYZ.12; HTML_BitRateBucketCsv=0,19083,16715,0,0,0,0,0; HTML_VisitValueCookie=1|1|1|0|35798|35826|0|0|0|0|0|0|NaN; s_pers=%20s_fid%3D22C0AF24132A0778-001FDBB2DA7591AD%7C1620284117936%3B%20s_c20%3D1557125717941%7C1651733717941%3B%20s_c20_s%3DFirst%2520Visit%7C1557127517941%3B; HTML_isPlayingCount=2; GED_PLAYLIST_ACTIVITY=W3sidSI6IlhYU0wiLCJ0c2wiOjE1NTcxMjU3MzgsIm52IjowLCJ1cHQiOjE1NTcxMjU1NDQsImx0IjoxNTU3MTI1NjM3fSx7InUiOiIzbnlXIiwidHNsIjoxNTU3MTI1NzM3LCJudiI6MCwidXB0IjoxNTU3MTI1NTU2LCJsdCI6MTU1NzEyNTYyM30seyJ1IjoiWG81TSIsInRzbCI6MTU1NzEyNTczNywibnYiOjEsInVwdCI6MTU1NzEyNTU4NSwibHQiOjE1NTcxMjU3MzV9XQ..; HTML_VisitCountCookie=1'}
        self.filter_url = 'http://console.cc.clipclaps.tv/crawler/log'
        self.post_url = 'http://127.0.0.1:30008/crawler/article/transfer'
        self.downloadPath = '/data/crawler'
        self.picPath = '/abc_news/picture/'



    def parsing_abcNews_list(self):
        today = self.point_time
        for kw in self.key_word:
            news_list = self.news_api.get_everything(q = kw,
                                                  sources = 'abc-news',
                                                  domains = 'abcnews.go.com',
                                                  from_param = today,
                                                  to = today[:-1]+str(int(today[-1])-1),
                                                  language = 'en',
                                                  sort_by = 'relevancy',
                                                  page_size = 100,)
            self.parsing_news_list_url(news_list=news_list)
            time.sleep(random.uniform(60, 70))


    def parsing_news_list_url(self, news_list):
        articles = news_list['articles']
        for i in range(len(articles)):
            details_url = articles[i]['url']
            result = self.filter_data(details_url=details_url)
            if result == '数据已存在':
                print('数据已存在')
            else:
                time.sleep(random.uniform(0, 5))
                details_res = requests.get(details_url, headers=self.headers, cookies=self.cookies).text
                html_obj = etree.HTML(details_res)
                sourceUrl = details_url
                jobId = time.time()
                authorName = articles[i]['source']['name']
                releaseTime = articles[i]['publishedAt']
                title_source = articles[i]['title']
                title = self.parsing_news_title(html_obj=html_obj, title_source=title_source)
                content = self.parsing_news_content(content_html=details_res)
                thumbnail_img = articles[i]['urlToImage']
                img = self.download_img(html_obj=html_obj, thumbnail_img=thumbnail_img)
                if img is None or img == '':
                    pass
                else:
                    data = {'jobId': int(jobId), 'sourceUrl': sourceUrl, 'title': title, 'authorName': authorName,
                            'releaseTime': releaseTime, 'content': content, 'img': img}
                    print('data:\n', data)
                    self.save_data(data=data)


    def parsing_news_title(self, html_obj, title_source):
        title = ''.join(html_obj.xpath('//header[@class="article-header"]//h1/text()'))
        if title == '' or title is None:
            return title_source
        else:
            return title


    def parsing_news_content(self, content_html):
        text = fulltext(content_html).split('\n')
        txt = list(filter(lambda x: x.strip() != '', text))
        content = '<p>'.join(txt)
        return content


    def download_img(self, html_obj, thumbnail_img):
        try:
            pic_url_list = html_obj.xpath('//figure//div//picture//img/@src')
            img_id = uuid.uuid4()
            index = 1
            img_list = []
            if pic_url_list == []:
                urllib.request.urlretrieve(thumbnail_img, r'%s.jpg' % (self.downloadPath + self.picPath + str(img_id) + "-" + str(index)))
                img = r'%s.jpg' % (self.picPath + str(img_id) + "-" + str(index))
                return img
            else:
                for pic_url in pic_url_list:
                    urllib.request.urlretrieve(pic_url, r'%s.jpg' % (self.downloadPath + self.picPath + str(img_id) + "-" + str(index)))
                    img_list.append(r'%s.jpg' % (self.picPath + str(img_id) + "-" + str(index)))
                    index += 1
                img = ','.join(img_list)
                return img
        except:
            pass


    def filter_data(self, details_url):
        data1 = urllib.parse.urlencode({
            'type': int(5),
            'days': int(3),
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.filter_url, data=data2)
        status = re.read().decode('utf-8')
        result = json.loads(status)
        data = result['data']
        data_list = []
        for kw in data:
            data_list.append(data[kw])
        if details_url in data_list:
            return '数据已存在'
        else:
            return details_url


    # 数据入库 post请求
    def save_data(self, data):
        data1 = urllib.parse.urlencode({
            'source': 4,
            'jobId': data['jobId'],
            'sourceUrl': data['sourceUrl'],
            'title': data['title'],
            'authorName': data['authorName'],
            'releaseTime': data['releaseTime'],
            'content': data['content'],
            'img': data['img'],
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.post_url, data=data2)
        status = re.read().decode('utf-8')
        print('status:\n', status)


if __name__ == '__main__':
    abc = ABC_News()
    try:
        abc.parsing_abcNews_list()
    except:
        pass

```



# 2019.5.5

**今天准备先将bbc news 进行登录认证，先判断抓取数据时候返回值让登录认证的时候先传data参数，看看会不会了， 还会的话进行判断，break 跳出本次数据爬取。**

**继续分析ap news 对其返回的script 进行解析**

```python
import requests, time, uuid, random, re, json
from lxml import etree
from newspaper import fulltext
import urllib.request
import urllib.parse



class Associated_Press_News(object):
    def __init__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        self.cookies = {'cookie': '_cb_ls=1; _cb=ChGdwsejPcBwqK1A; _ga=GA1.2.1067424464.1556266698; __gads=ID=b2804ef9280ce726:T=1556266708:S=ALNI_MbsZp6KMsLTd9MAhzM98UpWqF4sEQ; __qca=P0-112096547-1556266838413; trc_cookie_storage=taboola%2520global%253Auser-id%3Dbfc0c49d-bde0-4b78-9484-33cd8cb7509f-tuct3bdf4f1; GED_PLAYLIST_ACTIVITY=W3sidSI6Ilp4Q0YiLCJ0c2wiOjE1NTY2MTc5NjcsIm52IjowLCJ1cHQiOjE1NTY2MTc5NjAsImx0IjoxNTU2NjE3OTYwfV0.; _gid=GA1.2.1304411157.1557027854; _cb_svref=null; OptanonConsent=landingPath=NotLandingPage&datestamp=Sun+May+05+2019+11%3A44%3A56+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=4.1.0&EU=false&groups=0_140011%3A1%2C1%3A1%2C0_140010%3A1%2C2%3A1%2C3%3A1%2C4%3A1%2C0_140046%3A1%2C0_140042%3A1%2C0_140038%3A1%2C0_140034%3A1%2C0_140055%3A1%2C0_140051%3A1%2C0_140047%3A1%2C0_140043%3A1%2C0_140039%3A1%2C0_140035%3A1%2C0_140031%3A1%2C0_140052%3A1%2C0_140048%3A1%2C0_140044%3A1%2C0_140040%3A1%2C0_140036%3A1%2C0_140032%3A1%2C0_140053%3A1%2C0_140049%3A1%2C0_140045%3A1%2C0_140041%3A1%2C0_140037%3A1%2C0_140033%3A1%2C0_140054%3A1%2C0_140050%3A1%2C101%3A1%2C102%3A1%2C103%3A1%2C104%3A1%2C105%3A1%2C106%3A1%2C107%3A1%2C108%3A1%2C109%3A1%2C110%3A1%2C111%3A1%2C112%3A1%2C113%3A1%2C114%3A1%2C115%3A1%2C116%3A1%2C117%3A1%2C118%3A1%2C119%3A1%2C120%3A1%2C121%3A1%2C122%3A1%2C123%3A1%2C124%3A1%2C125%3A1%2C126%3A1%2C127%3A1%2C128%3A1%2C129%3A1%2C130%3A1%2C131%3A1%2C132%3A1%2C133%3A1%2C134%3A1%2C135%3A1%2C136%3A1%2C137%3A1%2C138%3A1%2C139%3A1%2C140%3A1%2C141%3A1%2C142%3A1%2C143%3A1%2C144%3A1%2C145%3A1%2C146%3A1%2C147%3A1%2C148%3A1%2C149%3A1%2C150%3A1%2C151%3A1%2C152%3A1%2C153%3A1%2C154%3A1%2C155%3A1&AwaitingReconsent=false; _tb_sess_r=; _tb_t_ppg=https%3A//apnews.com/245117b7dafd4790ba3d51db06cf345a; _gat=1; _chartbeat2=.1556266696382.1557028669628.1111100001.Vfd8vwJvnJujXq7Dq7JmkgXZfl.4'}
        self.post_url = 'http://127.0.0.1:30008/crawler/article/transfer'
        self.downloadPath = '/data/crawler'
        self.picPath = '/ap_news/picture/'
        self.filter_url = 'http://console.cc.clipclaps.tv/crawler/log'


    def run(self):
        try:
            news_dic = {
                'top' : 'https://apnews.com/apf-topnews',
                'sport' : 'https://apnews.com/apf-sports',
                'entertainment' : 'https://apnews.com/apf-entertainment',
                'travel' : 'https://apnews.com/apf-Travel',
                'technology' : 'https://apnews.com/apf-technology',
                'lifestyle' : 'https://apnews.com/apf-lifestyle',
                'business' : 'https://apnews.com/apf-business',
                'usNews' : 'https://apnews.com/apf-usnews',
                'health' : 'https://apnews.com/apf-Health',
                'science' : 'https://apnews.com/apf-science',
                'intlNews' : 'https://apnews.com/apf-intlnews',
                'politics' : 'https://apnews.com/apf-politics',
            }
            for url in news_dic:
                print('newsUlr:\n', url)
                ap.parsing_news_list_page(news_start_url=news_dic[url])
        except :
            pass


    def parsing_news_list_page(self, news_start_url):
        time.sleep(random.uniform(1, 30))
        list_page_html = requests.get(url=news_start_url, headers=self.headers, cookies=self.cookies).text
        list_html_obj = etree.HTML(list_page_html)
        list_page_url = list_html_obj.xpath('//a[@class="headline"]/@href')
        list_url = ['https://apnews.com' + i for i in list_page_url if 'https://apnews.com' not in i]
        for details_url in list_url:
            result=self.filter_data(details_url=details_url)
            if result == '数据已存在':
                print('数据已存在!')
            else:
                data = self.parsing_details_page(details_url=details_url)
                if data is None or data == {}:
                    pass
                else:
                    print('data:\n', data)
                    self.save_data(data=data)


    def parsing_details_page(self, details_url):
        time.sleep(random.uniform(1, 5))
        details_html = requests.get(url=details_url, headers = self.headers, cookies = self.cookies).text
        html_obj = etree.HTML(details_html)
        sourceUrl = details_url
        jobId = time.time()
        title = ''.join(html_obj.xpath('//div[@class="headline"]//h1/text()'))
        authorName = ''.join(html_obj.xpath('//span[@class="byline"]/text()'))
        releaseTime = ''.join(html_obj.xpath('//span[@class="Timestamp"]/@data-source'))
        content = self.parsing_news_content(content_html =details_html)
        img_urls = html_obj.xpath('//a[@class="LeadFeature LeadFeature_gallery"]/@href')
        if img_urls == [] or img_urls is None:
            pass
        else:
            img = self.download_picture(html=details_html)
            return {'jobId': int(jobId), 'sourceUrl': sourceUrl, 'title': title, 'authorName': authorName,
                    'releaseTime': releaseTime, 'content': content, 'img': img}


    def parsing_news_content(self, content_html):
        text = fulltext(content_html).split('\n')
        txt = list(filter(lambda x: x.strip() != '', text))
        content = '<p>'.join(txt)
        return content


    def download_picture(self, html):
        url_list = self.analysis_pic_url(html=html)
        img_id = uuid.uuid4()
        index = 1
        img_list = []
        for pic_url in url_list:
            urllib.request.urlretrieve(pic_url, r'%s.jpg' % (self.downloadPath + self.picPath + str(img_id) + "-" + str(index)))
            img_list.append(r'%s.jpg' % (self.picPath + str(img_id) + "-" + str(index)))
            index += 1
        img = ','.join(img_list)
        return img


    def analysis_pic_url(self,  html):
        html_script = r'<script>(.*?)</script>'
        script = re.findall(html_script, html, re.S | re.M)
        mediumIds_rule = r'mediumIds(.*?)]'
        rule = re.compile(mediumIds_rule)
        result = rule.findall(script[0])[0][3:]
        result = "[" + result + "]"
        js = json.loads(result)
        url_list = []
        for i in js:
            url = 'https://storage.googleapis.com/afs-prod/media/' + i + '/' + '600.jpeg'
            url_list.append(url)
        return url_list


    def filter_data(self ,details_url):
        data1 = urllib.parse.urlencode({
            'type': int(5),
            'days': int(3),
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.filter_url, data=data2)
        status = re.read().decode('utf-8')
        result = json.loads(status)
        data = result['data']
        data_list = []
        for kw in data:
            data_list.append(data[kw])
        if details_url in data_list:
            return '数据已存在'
        else:
            return details_url


    # 数据入库 post请求
    def save_data(self, data):
        data1 = urllib.parse.urlencode({
            'source': 6,
            'jobId': data['jobId'],
            'sourceUrl': data['sourceUrl'],
            'title': data['title'],
            'authorName': data['authorName'],
            'releaseTime': data['releaseTime'],
            'content': data['content'],
            'img': data['img'],
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.post_url, data=data2)
        status = re.read().decode('utf-8')
        print('status:\n', status)



if __name__ == '__main__':
    ap =Associated_Press_News()
    ap.run()


```





# 2019.4.30

**对AP News 多图新闻进行分析，爬取至少三张图，利用抓到文章首页图片地址，然后继续访问该图片地址，该图片地址包含三张图，但是加载其他图是AJAX异步请求，需要继续分析**



#2019.4.29

**解析AP News 并将其部署到服务器，进行数据入库,对BBC News 利用 News API 和 Newspaper 进行解析，但是发现NewsAPI 每次访问500次就不会返回数据（个人版AP Key），故每天只能返回一定量新闻数据。**

#2019.4.28

**将TopBuzz视屏爬取并入库，cbs News分栏目爬取数据并入库**

**研读 newspaper 解析HTML页面及其抓取原理，并尝试优化**

**分析 AP news** 

**分析 YouTuBe 视屏网站并爬取入库**

```python
import requests
from lxml import etree
import time ,json, uuid, re
import urllib.request
import urllib.parse
import hashlib ,random



class TopBuzzVideo():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2 MIUI/V10.2.2.0.ODECNXM) NewsArticle/8.4.4',
                }
        self.cookies = {
                    'cookies': 'install_id=6672646082571388678; ttreq=1$a9ed7f4ce8fc84fced473d6e25c22226f381c13d; odin_tt=3e76568447d177856560d524c6ef5400407a437cfdd62767a36fb3b2decdeb01d43b9a7978232dc05c57af3c81bd10c277e78619093795e8392c1302c9aa8a75; sid_guard=c8f84a23bcce86b376964aeb42991709%7C1554173959%7C5184000%7CSat%2C+01-Jun-2019+02%3A59%3A19+GMT; uid_tt=2ad7176029f7302e11b7924e6e6566b7120075732cedcd39bc999fa5cbcf07a1; sid_tt=c8f84a23bcce86b376964aeb42991709; sessionid=c8f84a23bcce86b376964aeb42991709',
                }
        self.headers_details = {
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                }
        self.cookies_details = {
                    'Cookie': 'tt_webid=6683297640216282629; __tea_sdk__user_unique_id=6683297640216282629; __tea_sdk__ssid=40d2e59e-696c-4a93-ace8-e1479b10aeef; csrf-token=61575f8b568b577d9d06c777d103ae53e6c10723; csrf-secret=6qDUsFL6WZ1aG2soaPw7PpmCtnxCv7fw'
                }
        self.post_video_url = 'http://127.0.0.1:30008/crawler/video/transfer'


    def run(self):
        number = 0
        while number < 11:
            t = time.time()
            result = re.findall('.\d*', str(t))   # 正则匹配时间戳小数位
            sign = tb.hash_code(result[1][1:])    # 对时间戳进行解密
            timestamp = result[0]
            start_url = 'https://i16-tb.isnssdk.com/api/844/stream?session_impr_id=0&tab=General&count=20&min_behot_time=1.554174097999E9&loc_mode=7&lac=4314&cid=6439033' \
                  '&sign=' + sign + \
                  '&timestamp=' + timestamp + \
                  '&logo=topbuzz&gender=0&bv_is_auto_play=0&youtube=0&manifest_version_code=844&app_version=8.4.4&iid=6672646082571388678&gaid=54b268f4-52c2-470c-a815-abd1d00acce9&original_channel=gp&channel=gp&fp=TlTrJzK1FYsqFYs5PlU1LMGSL2Xr&device_type=MIX+2&language=en&app_version_minor=8.4.4.01&resolution=2030*1080&openudid=ab50caa43e995042&update_version_code=8440&sys_language=zh&sys_region=cn&os_api=26&tz_name=Asia%2FShanghai&tz_offset=28800&dpi=440&brand=Xiaomi&ac=WIFI&device_id=6672637176796333574&os=android&os_version=8.0.0&version_code=844&hevc_supported=1&device_brand=Xiaomi&device_platform=android&sim_region=cn&region=us&aid=1106&ui_language=en'
            tb.analysis_topBuzz(start_url=start_url)
            number += 1
            time.sleep(random.uniform(60, 70))    # 每隔 1min 进行一次访问


    def hash_code(self, pwd):
        # 通过模块构造出一个hash对象
        h = hashlib.sha1()
        h.update(pwd.encode())
        # 获得字符串类型的加密后的密文
        return h.hexdigest()

    def analysis_topBuzz(self, start_url):
        try:
            time.sleep(random.uniform(0, 3))
            res = requests.post(url=start_url, headers=self.headers, cookies=self.cookies).text
            data = json.loads(res)
            item = data['data']['items']
            # 分析列表页，获得详情页url
            for i in range(len(item)):
                cls = item[i]['article_class']
                if cls == 'Video':
                    share_url = item[i]['share_url']
                    video_url = item[i]['video']['url_list'][0]['urls'][0]
                    data = self.parsing_details_url(details_url=share_url, video_url=video_url)
                    print('analysis_topBuzz_data:\n', data)
                    self.save_video(data = data)
        except:
            pass


    def parsing_details_url(self, details_url=None, video_url=None):
        time.sleep(random.uniform(0, 3))
        result = requests.get(url=details_url, headers=self.headers_details, cookies=self.cookies_details).text
        html = etree.HTML(result)
        # 调度任务
        jobId = time.time()
        # 文章标题
        title = html.xpath('//div[@class="title"]/text()')[0]
        # 作者
        authorName = ' '.join(html.xpath('//div[@class="name active"]/text()'))
        if authorName == '':
            authorName = ' '.join(html.xpath('//div[@class="name"]/text()'))
        # 文章发布时间
        releaseTime = ' '.join(html.xpath('//div[@class="publishTime"]/text()'))
        # 视频
        video = self.download_video(videoUrl=video_url)

        return {'jobId': jobId, 'sourceUrl': details_url, 'title': title, 'authorName': authorName,
                'releaseTime': releaseTime, 'video': video}

    def download_video(self, videoUrl):
        videoId = uuid.uuid4()
        downloadPath = '/data/crawler'
        videoPath = '/topbuzz/video/'
        urllib.request.urlretrieve(videoUrl, r'%s.mp4' % (downloadPath + videoPath + str(videoId)))
        video = '%s.mp4' % (videoPath + str(videoId))
        return video

    def save_video(self, data):
        data1 = urllib.parse.urlencode({
            'source': 1,
            'sourceUrl': data['sourceUrl'],
            'title': data['title'],
            'authorName': data['authorName'],
            'releaseTime': data['releaseTime'],
            'video': data['video'],
        })
        data2 = data1.encode('utf-8')
        re = urllib.request.urlopen(url=self.post_video_url, data=data2)
        status = re.read().decode('utf-8')
        print('status:\n', status)

if __name__ == '__main__':
    tb = TopBuzzVideo()
    try:
        tb.run()
    except BaseException as e:
        print('run_error:\n', e)

```



# 2019.4.24

**取消BuzzFeed项目中Shooping字段，并将SmartNews部署到172服务器，运行172服务器上爬虫服务,分析TOPBuzz爬虫视频**
**了解Fsherp编程语言，下载安装DotNet、VSCode,并了解熟悉使用**




# 2019.4.23

**今天任务先将4.22版本代码存放在github上，继续分析Smart News and Flip Board 两个源**

**今天运营开始测试文本内容，发现Bug如下：**

> > **```1.多图文本少，增加多图文本；```**

> > **```2.文章断片，只有一部分文本，丢失了一部分文本；```**

> > **```3.将视频爬取添加进任务列表 ```**

**app源SmartNews解析：Post请求，传参：headers，data，无cookies**

```python
import requests
import json


class SmartNews():
    def __init__(self):
        self.headers = {'User-Agent': 'SmartNews 5.4.3 (Android 8.0.0; zh_CN; MIX 2 Build/OPR1.170623.027)'}
        self.data = {
                    'Accept-Encoding':'gzip',
                    'Content-Length':'397',
                    'Content-Type':'application/x-www-form-urlencoded',
                    'Host':'www.smartnews.be',
                    'Connection':'keep-alive',
                    'deviceToken':'gw73n3ddMfRttJlu-YVFdw',
                    'timestamp':'1556004832',
                    'version':'20140105.1.android',
                    'edition':'en_ALL',
                    'timezone':'Asia/Shanghai',
                    'locale':'zh_cn',
                    'language':'zh',
                    'country':'cn',
                    'useUnifiedChannels':'true',
                    'channelIdentifiers':'cr_en_all_sports,cr_en_all_entertainment,cr_en_all_world,cr_en_all_business,cr_en_all_technology,cr_en_all_science,cr_en_all_lifestyle,cr_en_all_twitter',
                    'since':'1555916243956',
                    }
        self.url = 'http://www.smartnews.be/api/v2/refresh'
        self.detailUrl='http://sf-proxy.smartnews.com/https%3A%2F%2Fthriveglobal.com%2Fstories%2Fwhy-vision-and-mission-really-do-matter%2F?etag=4e420c3234fdf77326f69071250655fa'


    def smartNews(self):
        res = requests.post(url = self.url, headers = self.headers, data = self.data).text
        data = json.loads(res)
        items = data["items"]
        blocks = []
        for i in items:
            blocks += i['blocks']
        links = []
        for j in blocks:
            links += j['links']
        url_list = []
        for u in links:
            url_list.append(u['url'])
        return url_list


if __name__ == '__main__':
    sm = SmartNews()
    sm.smartNews()


```



# 2019.4.22

**向运营要新的app源，进行爬取，对已经部署到5.232、15.11两个服务器上的代码进行测试维护更新，保证代码随时待命可以运行。**

```
flipboard账号:
Zhang Peng
zhangpeng@clipclaps.com
5Y6LcMzxqyHPdj8
```

**分析爬取Smart News 和 Flip Board ，将之前4.19的爬虫项目更新到4.22，在232服务器上运行两次入库差不多有500+数据**

```
![爬虫app][/Users/mr.zhang/Desktop/mynotes/clipclaps/app爬虫.jpg]
```



# 2019.4.19

​	**将新增字段后的 code 重新测试，保证运行正常后部署到 15.11 的服务器上进行运行测试，无误后再部署到5.232 服务器上时刻保证代码的统一性**

​	**一个稳定项目部署到服务器上都有自己明确的稳定的版本号记录，新的版本可以保持开发，但旧版本也得一直保持其正常的运行，每个程序员的代码也得有自己的版本号，每天记录下自己的开发过程，记录下来，方便管理的同时，也更加明确自己的任务。**

​	**tig 让 git命令行可视化 ,方便管理git上的code版本**

​	```brew  install …..```

​	**代码严禁多行注释，通过判断调用来解决不同的需求，代码应该适配多种情况**

​	

# 2019.4.18

​	**查看TopBuz爬取内容，统计爬取数据，将BuzzFeed新增了一些字段来爬取内容，效果还挺好的，其中BuzzFeed遇到一个BUG：```requests.exceptions.SSLError: HTTPSConnectionPool(host='www.buzzfeednews.com', port=443): Max retries exceeded with url: /us/feed/home?page=1&flexpro_enabled=1 (Caused by SSLError(SSLError(1, '[SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:719)'),))```**

##### 解决办法：```you can pip install pyOpenSSL or Use the anaconda environment```



# 2019.4.17

​	**服务器安装git，将代码部署到 ssh 10.1.5.232 服务器，进行post入库，对代码爬取数量进行统计，对多图数据进行入库统计。**

​	**下午将代码部署到了10.1.5.232 服务器上，项目运行正常，TopBuzz 爬取无内容，怀疑视频多，过滤掉了**



# 2019.4.16

​	**对GoogleNews数据进行分析，对返回的数据进行测试入库。分析其他爬虫手段。对代码进行修复，google-news返回数据入mysql没问题。熟悉Phabricator。**

### ```>>> Reddit新闻源API```              

##GoogleNews

```python
from newsapi import NewsApiClient
from bs4 import BeautifulSoup as soup
import urllib.request
import ssl
import time
try:
    from news_project.newsfeeds import NewsFeeds
except:
    import sys
    sys.path.append('news_project')
    from newsfeeds import NewsFeeds


class GoogleNews():
    def __init__(self):
        self.news_api = NewsApiClient(api_key='cb7a4ae15a98429890aeedb9a7b460a0')
        self.key_word = ['Latest','World','U.S.','Business', 'Technology', 'Entertainment', 'Sports', 'Science', 'Health']
        self.t = time.time()
        self.point_time = time.strftime('%Y-%m-%d', time.localtime(self.t))
        self.google_crawler = 1


    def googleNews(self):

        if self.google_crawler == 1:
            # 从google新闻中获取热门新闻
            news_url = "https://news.google.com/news/rss"
            ssl._create_default_https_context = ssl._create_unverified_context
            Client = urllib.request.urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page, "xml")
            news_list = soup_page.findAll("item")
            return news_list

        elif self.google_crawler == 2:
            # 返回 google-news 指定日期和分类的资讯
            today = self.point_time
            url_list = []
            for kw in self.key_word:
                all_articles = self.news_api.get_everything(q = kw,
                                                      sources = 'google-news',
                                                      domains = 'news.google.com',
                                                      from_param = today,
                                                      to = today[:-1]+str(int(today[-1])-1),
                                                      language = 'en',
                                                      sort_by = 'relevancy',
                                                      page_size = 100,)
                articles = all_articles['articles']
                for i in range(len(articles)):
                    url = articles[i]['url']
                    url_list.append(url)
            return url_list

        else:
            # 返回google-news的头条新闻
            top_headlines = self.news_api.get_top_headlines(
                                                        sources = 'google-news',
                                                        language='en',
                                                        page_size = 100,
                                                       )

            articles = top_headlines['articles']
            url_list=[]
            for i in range(len(articles)):
                url = articles[i]['url']
                url_list.append(url)
            return url_list

if __name__ == '__main__':
    g = GoogleNews()
    t = g.t
    today = g.point_time
    t2 = g.point_time
    print(today)
    print()

```



# 2019.4.15

​	**对GoogleNews进行APP页面分析，按分类爬取数据，返回了一些数据，入库有问题会报错，熟悉软件开发平台Phabricator，Phabricator 是一套基于web的软件开发工具，它针对git项目的代码管理工具，可以跟踪bug、记录需求、wiki编写**



# 2019.4.13

​	**将多图code部署到服务器，项目运行入库，图片质量不高，查看newspaper源代码，找他的抓取图片url底层实现，查看是否可以优化ocde，底层利用PIL对图片进行处理。**



# 2019.4.12

​	**测试多图情况下任务爬取情况，任务数据输出量，分析新app LifeBuzz**

​	**将多图根据尺寸进行判断，对于尺寸大于(150,150)的图进行入库**

```python
    # 获取图片尺寸，按要求下载
    def getPicSize(self, picUrls, downloadPath, picPath):
        img_id = uuid.uuid4()
        index = 1
        imgList = []
        # 利用 Validators.url 判断解析出来的url是否是正确的
        href_list = [href for href in picUrls  if validators.url(href) == True]
        for url in href_list:
            req = requests.get(url)
            im = Image.open(BytesIO(req.content))
            pic_path = '%s.jpg' % (picPath + str(img_id) + '-' + str(index))
            if im.size[0] > 50 and im.size[1]>50:
                # urllib.request.urlretrieve(url,r'%s.jpg' % (downloadPath+picPath+str(img_id)+"-"+str(index)))
                imgList.append(pic_path)
                index += 1
        img = ','.join(imgList)
        return img

```



# 2019.4.11

​	**将TopBuzz进行页面分析，查看运行返回None值原因，对app爬取数据进行统计，每运行一个周期返回数据量多少，去重后的数据量多少，以及每个app消息推送周期多长时间，爬虫定时任务部署的运行周期多久合适，添加多图筛选，去除无图的文本。**

​	**TopBuzz、NewsBreak返回None或报错原因是此时间段内无新咨询推送，每天按8小时任务，不考虑遇到封IP或者其他因素，每天理想状态下TopBuzz，BuzzFeed，NewsBreak三个APP一共可以爬取2400+800+2400=5600条数据，先由于筛选多图文章，目前没有完整的测试过数据量。**



#2019.4.10

​	**将TopBuzz、BuzzFeed、NewsBreak三个APP进行封装，已部署到服务器进行运行，入库和url去重正常，但TopBuzz时常返回None值，怀疑app端无新消息、或封ip（换ip依旧有返回None值得时候，怀疑无新消息）**

##TopBuzz

```python
import requests
import time
import json
import re
import hashlib
try:
    from news_project.newsfeeds import NewsFeeds
except:
    import sys
    sys.path.append('news_project')
    from newsfeeds import NewsFeeds


class TopBuzz():
    def __init__(self):
        # 请求头信息
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2 MIUI/V10.2.2.0.ODECNXM) NewsArticle/8.4.4'
        }
        self.cookies = {
            'cookies': 'install_id=6672646082571388678; ttreq=1$a9ed7f4ce8fc84fced473d6e25c22226f381c13d; odin_tt=3e76568447d177856560d524c6ef5400407a437cfdd62767a36fb3b2decdeb01d43b9a7978232dc05c57af3c81bd10c277e78619093795e8392c1302c9aa8a75; sid_guard=c8f84a23bcce86b376964aeb42991709%7C1554173959%7C5184000%7CSat%2C+01-Jun-2019+02%3A59%3A19+GMT; uid_tt=2ad7176029f7302e11b7924e6e6566b7120075732cedcd39bc999fa5cbcf07a1; sid_tt=c8f84a23bcce86b376964aeb42991709; sessionid=c8f84a23bcce86b376964aeb42991709',
        }


    # TopBuzz列表页时间戳解析
    def hash_code(self, pwd):
        # 通过模块构造出一个hash对象
        h = hashlib.sha1()
        h.update(pwd.encode())
        # 获得字符串类型的加密后的密文
        return h.hexdigest()


    # TopBuzz解析列表页面
    def sendRequest(self, url):
        try:
            res = requests.post(url=url, headers=self.headers, cookies=self.cookies).text
            data = json.loads(res)
            item = data['data']['items']
            # 分析获取的json
            urlList=[]
            for i in range(len(item)):
                # 数据来源
                sourceUrl = item[i]['article_url']
                urlList.append(sourceUrl)
            return urlList

        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'TopBuzzSendRequest\t', str(e))




if __name__ == '__main__':
        tb=TopBuzz()
        # 访问时间
        t = time.time()
        #正则匹配时间戳小数位
        result=re.findall('.\d*',str(t))
        sign=tb.hash_code(result[1][1:])
        timestamp=result[0]

        url = 'https://i16-tb.isnssdk.com/api/844/stream?session_impr_id=0&tab=General&count=20&min_behot_time=1.554174097999E9&loc_mode=7&lac=4314&cid=6439033' \
              '&sign='+sign+ \
              '&timestamp='+timestamp+ \
              '&logo=topbuzz&gender=0&bv_is_auto_play=0&youtube=0&manifest_version_code=844&app_version=8.4.4&iid=6672646082571388678&gaid=54b268f4-52c2-470c-a815-abd1d00acce9&original_channel=gp&channel=gp&fp=TlTrJzK1FYsqFYs5PlU1LMGSL2Xr&device_type=MIX+2&language=en&app_version_minor=8.4.4.01&resolution=2030*1080&openudid=ab50caa43e995042&update_version_code=8440&sys_language=zh&sys_region=cn&os_api=26&tz_name=Asia%2FShanghai&tz_offset=28800&dpi=440&brand=Xiaomi&ac=WIFI&device_id=6672637176796333574&os=android&os_version=8.0.0&version_code=844&hevc_supported=1&device_brand=Xiaomi&device_platform=android&sim_region=cn&region=us&aid=1106&ui_language=en'

        a=tb.sendRequest(url=url)
        print(a)


```



## BuzzFeed

```python
import requests
from lxml import etree
import time, json
try:
    from news_project.newsfeeds import NewsFeeds
except:
    import sys
    sys.path.append('news_project')
    from newsfeeds import NewsFeeds



class BuzzFeed():
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
        self.cookies = {
            'cookie': '_ga=GA1.2.980887030.1554094864; __qca=P0-370898470-1554094864412; permutive-id=4b0388f5-cd06-48fb-bc43-3bd5b284a15f; __gads=ID=7ed4ac47516d0c08:T=1554094874:S=ALNI_Mb5hT5yTksr6ehByJBrLYY7lWInBA; _fbp=fb.1.1554094878563.234463870; ads_amazon_tam=on; ads_amazon_tam_version=1; ads_ad_lightning=on; ads_ad_lightning_version=1; ads_prebid=on; ads_prebid_version=1; ADSGROUP-699-outbrain-redux=control; ADSGROUP-699-outbrain-redux_version=2; ad_exchange_vox_concert=inline; ad_exchange_vox_concert_version=3; ads_scroll_subscription=on; ads_scroll_subscription_version=1; advertise_international=on; advertise_international_version=1; moat_dfp_native_video_tracking=on; moat_dfp_native_video_tracking_version=1; ADSGROUP-442-permutive=on; ADSGROUP-442-permutive_version=1; non_us_ad_lookahead_adjustments=on; non_us_ad_lookahead_adjustments_version=1; ads_adrizer=on; ads_adrizer_version=1; ADSGROUP-1015_awareness_billboard=billboard; ADSGROUP-1015_awareness_billboard_version=1; _cmpQcif3pcsupported=1; _gid=GA1.2.1718839625.1554714335; ads_inline_density_bfnews=density-250; ads_inline_density_bfnews_version=2; bfn_recirc_popup=control; bfn_recirc_popup_version=1; ad_display_card_sticky=control; ad_display_card_sticky_version=2; bfn_newsletter_popup=on; bfn_newsletter_popup_version=1; bfn_support_text=role; bfn_support_text_version=1; bf_nb_pp_dismissed=true; _pdfps=%5B7684%2C13160%2C13164%2C13730%2C10915%2C12448%2C12449%2C12882%2C13675%2C12244%2C14140%2C14192%2C10222%2C10788%2C10216%2C13098%2C13162%2C13276%2C13319%2C14110%2C14144%2C%2212244-15-22969%22%2C%2212244-15-22970%22%2C%2213458-15-22969%22%2C%2213458-15-22970%22%2C%2213459-15-22969%22%2C%2213459-15-22970%22%2C%2213524-2-294%22%2C%2214140-2-6723%22%2C%2214147-2-292%22%2C%2214351-15-22835%22%5D; _gat=1; sailthru_pageviews=12; permutive-session=%7B%22session_id%22%3A%22c440b2b2-d5b2-47da-a80a-a915417b28f6%22%2C%22last_updated%22%3A%222019-04-08T09%3A19%3A31.428Z%22%7D; sailthru_content=4aabfd73798a801ca4c9a396b30365ca5e49765b4283840f5c8259960590061f65292542d9dc5ee7cb5545f027fdd2b1f044956926b209e90497a64953e290f7; sailthru_visitor=6e0b676a-cfc5-4a77-bd49-98f70afc486f'
        }


    def parsingNewsUrl(self):
        try:
            pg = 1
            urls_news = []
            while pg < 6:
                new_url = 'https://www.buzzfeednews.com/us/feed/home?page=' + str(pg) + '&flexpro_enabled=1'
                res = requests.get(url=new_url, headers=self.headers, cookies=self.cookies).text
                html = etree.HTML(res)
                url_list = html.xpath('//div[@class="news-feed grid-layout-main"]//article/a/@href')
                urls_news += url_list
                pg += 1
            return urls_news
        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'BuzzFeedParsingNewsUrl]\t', str(e))

    def parsingTopUrl(self):
        try:
            pg = 1
            urls_tops = []
            while pg <6:
                top_url = 'https://www.buzzfeed.com/site-component/v1/en-us/morebuzz?page='+str(pg)+'&page_size=15&image_crop=wide'
                res = requests.get(url=top_url, headers=self.headers, cookies=self.cookies).text
                data = json.loads(res)
                results = data['results']
                for i in range(len(results)):
                    res_url = results[i]['url']
                    if res_url is None or res_url == '':
                        pass
                    urls_tops.append(res_url)
                pg += 1
            return urls_tops
        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'BuzzFeedParsingTopUrl]\t', str(e))

    def parsingHome(self):
        try:
            pg = 1
            urls_homes = []
            while pg < 6:
                home_url = 'https://www.buzzfeed.com/us/feedpage/feed/home?page='+str(pg)+'&page_name=home'
                res = requests.get(url=home_url, headers=self.headers, cookies=self.cookies).text
                html = etree.HTML(res)
                urls_list = html.xpath('//a[@class="js-card__link link-gray"]/@href')
                urls_homes += urls_list
                pg += 1
            return urls_homes
        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'BuzzFeedParsingHomeUrl]\t', str(e))

    def parsingQuizzes(self):
        try:
            pg = 1
            urls_quizzes = []
            while pg < 6:
                quizzes_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes?page='+str(pg)+'&page_name=quizzes'
                res = requests.get(url=quizzes_url, headers=self.headers, cookies=self.cookies).text
                html = etree.HTML(res)
                urls_list = html.xpath('//a[@class="js-card__link link-gray"]/@href')
                urls_quizzes += urls_list
                pg += 1
            return urls_quizzes
        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'BuzzFeedParsingQuizzesUrl]\t', str(e))

    def parsingShopping(self):
        try:
            pg = 1
            urls_shopping = []
            while pg < 6:
                shopping_url = 'https://www.buzzfeed.com/us/feedpage/feed/shopping?page='+str(pg)+'&page_name=shopping'
                res = requests.get(url=shopping_url, headers=self.headers, cookies=self.cookies).text
                html = etree.HTML(res)
                urls_list = html.xpath('//a[@class="js-card__link link-gray"]/@href')
                urls_shopping += urls_list
                pg += 1
            return urls_shopping
        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'BuzzFeedParsingShoppingUrl]\t', str(e))



if __name__ == '__main__':

    bz = BuzzFeed()
    # a=bz.parsingShopping()
    # bz.parsingNewsUrl()
    # a=bz.parsingTopUrl()
    a = bz.parsingHome()
    print(a)

```





## NewsBreak

```python
import requests
import json, time
try:
    from news_project.newsfeeds import NewsFeeds
except:
    import sys
    sys.path.append('news_project')
    from newsfeeds import NewsFeeds



class NewsBreak():
    def __init__(self):
        self.data = {
            "clientInfo": {
                "deviceInfo": {
                    "model": "MIX 2",
                    "device": "chiron",
                    "androidVersion": "8.0.0",
                    "screenWidth": 1080,
                    "screenHeight": 2030
                },
                "userInfo": {
                    "mac": "02:00:00:00:00:00",
                    "language": "zh",
                    "country": "CN",
                    "serviceProvider": "WIFI"
                }
            }
        }
        self.headers = {
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2 MIUI/V10.2.2.0.ODECNXM)',
        }
        self.cookies = {
            'JSESSIONID': 'bV9kSkqHnHWIWsl6YJ6Vuw',
        }

    # 解析Post请求，获取docid
    def parsingPost(self, url):
        try:

            res = requests.post(url= url, headers=self.headers, data= self.data, cookies= self.cookies).text
            data = json.loads(res)
            result = data['result']
            docList = []
            for i in result:
                try:
                    docList.append(i['docid'])
                except:
                    pass
            return ','.join(i for i in docList)

        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'NewsBreakPost', str(e))

    # 解析Get请求
    def parsingGet(self, url):
        try:
            res = requests.get(url, headers=self.headers, cookies=self.cookies).text
            data = json.loads(res)
            result = data["documents"]
            urlList=[]
            for i in range(len(result)):
                sourceUrl = result[i]['url']
                urlList.append(sourceUrl)
            return urlList
        except BaseException as e:
            NewsFeeds().point_log(str(NewsFeeds().localTime(time.time())), 'NewsBreakGet\t', str(e))



if __name__ == '__main__':
    post_url='http://api.particlenews.com/Website/channel/news-list-for-best-channel?cstart=0&infinite=true&refresh=1&epoch=5&distribution=newsbreak&platform=1&cv=4.7.3&cend=10&appid=newsbreak&weather=true&fields=docid&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=fb_share_total&fields=coach_mark_text&fields=up&fields=down&fields=summary&fields=favicon_id&fields=dominant_image&fields=contextMeta&fields=video_urls&fields=viewType&push_refresh=0&modularize=true&ts=2019-04-07+18%3A14%3A01+%2B0800&version=020025&net=wifi'

    nb=NewsBreak()
    docId=nb.parsingPost(url=post_url)
    get_url = 'http://api.particlenews.com/Website/contents/content?related_docs=false&cv=4.7.3' \
              '&docid=' + docId + \
              '&appid=newsbreak&bottom_channels=false&distribution=newsbreak&platform=1&version=020025&net=wifi'
    u=nb.parsingGet(url=get_url)
    print(u)

```















