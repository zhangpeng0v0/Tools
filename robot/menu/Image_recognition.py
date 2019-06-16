from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15650587'
API_KEY = 'l16MOL7rsgoKShXt4MTMFrHC'
SECRET_KEY = 'uuuqTMITd6ukqckWBc7fw9dM5ziqtm1c'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('F:/Virtual/机器学习/robot/img/2.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
result=client.basicGeneral(image)
print(result)