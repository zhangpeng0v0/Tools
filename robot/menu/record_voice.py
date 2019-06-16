"""
Description: 
录入语音
流程：采样-》写入文件
"""
import pyaudio
import wave
def record(seconds,filename):
    RATE=8000#采样率
    CHANNELS=2#采样管道数
    FORMAT=pyaudio.paInt16#量化位数
    SECONDS=seconds#录音时长
    #第一步：创建PyAudio的实例对象
    p = pyaudio.PyAudio()
    #第二步：调用PyAudio实例对象的open方法创建流Stream
    stream=p.open(rate=RATE,channels=CHANNELS,format=FORMAT,input=True)
    frames=[]#存储所有读取到的数据
    print("录音开始,还有",seconds,"秒")
    #第三步：根据需求，调用Stream的write或者read方法
    data=stream.read(RATE*SECONDS)
    frames.append(data)
    #第四步：调用Stream的stop方法停止播放音频或者是录制音频
    stream.stop_stream()
    print("录音结束！！！")
    #第五步：调用Stream的close方法，关闭流
    stream.close()
    #第六步：调用pyaudio.PyAudio.terminate() 关闭会话
    p.terminate()
    #写入到wav文件里面
    wf=wave.open(filename,"wb")
    wf.setnchannels(CHANNELS)
    wf.setframerate(RATE)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename
