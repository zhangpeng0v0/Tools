import pandas
import numpy
df=pandas.read_excel(r'E:\数据清洗\excel\数据3.xlsx')
for d in numpy.array(df).tolist():
    print(d)
#numpy.ndarray
