# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def loadData(filepath):  # 加载数据，并清洗数据
    names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
             'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
             'salary']
    table = pd.read_csv(
        filepath_or_buffer=filepath,
        sep=',',
        names=names
    )
    # 删除带?的行
    for key in table:
        try:
            table = table[~ table[key].str.contains('\?')]  # ?需要转译
        except:
            continue
    # 去重
    table.drop_duplicates(inplace=True)
    # 分割数据
    data_x = table.iloc[:, :14]
    data_y = table['salary']
    # 清洗x矩阵中的数据
    for i in ['workclass', 'education', 'marital-status', 'occupation',
              'relationship', 'race', 'sex', 'native-country']:
        uniqueValues = data_x[i].drop_duplicates()
        value_to_int = 0
        for value in uniqueValues:
            data_x[i].replace(to_replace=value, value=value_to_int, inplace=True)
            value_to_int += 1
    # 清洗y向量中的数据
    uniqueValues = data_y.drop_duplicates()
    value_to_int = 0
    for value in uniqueValues:
        data_y.replace(to_replace=value, value=value_to_int, inplace=True)
        value_to_int += 1
    return data_x, data_y


if __name__ == '__main__':
    train_file = r'data\adult.txt'
    test_file = r'data\adult_test.txt'
    train_x, train_y = loadData(train_file)
    test_x, test_y = loadData(test_file)

    # 朴素贝叶斯
    nbs = [GaussianNB(), BernoulliNB(), MultinomialNB()]
    for nb in nbs:
        nb.fit(train_x, train_y)
        print(nb.score(test_x, test_y))

    # 决策树
    tr = DecisionTreeClassifier()
    tr.fit(train_x, train_y)
    print(tr.score(test_x, test_y))

    # 决策森林
    forest = RandomForestClassifier(n_estimators=500)
    forest.fit(train_x, train_y)
    print(forest.score(test_x, test_y))

