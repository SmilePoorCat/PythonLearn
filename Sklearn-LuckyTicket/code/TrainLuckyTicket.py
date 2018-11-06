#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

train = pd.read_csv('../test_files/train_data.txt')
df = pd.DataFrame(train, columns=['data', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7'])
df.head(10)
test = pd.read_csv('../test_files/test_data.txt')

train['Type'] = 'Train'

test['Type'] = 'Test'

fullData = pd.concat([train, test], axis=0)  # 联合训练、测试数据集

fullData.columns # 显示所有的列名称

fullData.head(10) #显示数据框的前10条记录

fullData.describe() #你可以使用describe()函数查看数值域的概要
