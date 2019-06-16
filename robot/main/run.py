from robot.menu import record_voice, tuling , baidu_yuyin
from aip import AipSpeech

class Run_Game():
    def __init__(self):
        self.APP_ID = '15650587'
        self.API_KEY = 'l16MOL7rsgoKShXt4MTMFrHC'
        self.SECRET_KEY = 'uuuqTMITd6ukqckWBc7fw9dM5ziqtm1c'
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def voice(self):
        record_voice.record(3, 'voice.wav')  # 开始录音

    def tuling(self):
        res=tuling.get_result('你是傻子吗？')

    # 将录音转化成文字
    # 读取文件
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 识别本地文件
    resp = self.client.asr(get_file_content('vioce.wav'), 'wav', 16000, {
        'dev_pid': 1536,
    })

if __name__ == '__main__':
      r=Run_Game()
      r.tuling()






