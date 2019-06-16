"""
Description:
文字版聊天机器人
使用urllib发起请求，访问api接口，得到响应数据
"""
import urllib.request as req
import urllib.parse as parse

def get_result(question):
    #接口请求路径
    url="http://www.tuling123.com/openapi/api"
    #参数
    #第一个参数：聊天机器人apikey
    #第二个参数：问题
    #第三个参数：用户唯一标识，固定为12345678
    params={
        "key":"cca78744640c4bf2a24c6891e1e69a80",
        "info":question,
        "userid":"12345678"
    }
    #对参数编码，将字典形式的参数转为bytes形式
    params=parse.urlencode(params).encode("UTF8")
    #发起请求，获得响应流
    resp=req.urlopen(url,params)
    #读取响应流中的数据
    json=resp.read()
    #解析json串，提取出来所需数据
    print(eval(json))
    return eval(json)

get_result('你是魔鬼吗？')