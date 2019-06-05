import urllib.request
import urllib.parse

# get请求
def get(url,*args,**kwargs):
    '''

    :param url: 请求路径
    :param args: 预留
    :param kwargs: 预留
    :return:
    '''
    return urllib.request.urlopen(url).read()


# post请求
def post(url,*args,**kwargs):
    '''
    :param url:
    :param args:
    :param kwargs:
            postData:post数据
            postData:是一个字典
            charset:用于设置post数据的格式  ： 例如utf-8  gbk  utf-16
    :return:
    '''
    try:
        kwargs['charset']
    except:
        charset = 'utf-8'
    else:
        charset=kwargs['charset']

    data=urllib.parse.urlencode(kwargs['postData']).encode(charset)
    return urllib.request.urlopen(url,data=data).read()

