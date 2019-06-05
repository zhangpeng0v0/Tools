from win32com import client as wc
import os
word = wc.Dispatch('Word.Application')
for f in os.listdir(r'E:\数据清洗\test'):     #获取所有路径下的所有doc列表名称
    try:
        if f.endswith('.doc'):   #  endswith   获取后缀名称
            doc = word.Documents.Open(os.path.join(r'E:\数据清洗\test',f))        # 目标路径下的文件
            doc.SaveAs(os.path.join(r'E:\数据清洗\test',f.replace('doc','docx')), 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
            os.remove(os.path.join(r'E:\数据清洗\test',f))   #将文件转换成docx后删除掉doc文件
            doc.Close()
    except:
        print(f)
word.Quit()


# 如果想要转换成为   txt  将12改为4

