# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:08:46 2021

@author: Ahmed
"""

import pandas as pd

train = pd.read_csv('train.csv')
stores = pd.read_csv('stores.csv')
features = pd.read_csv('features.csv')

# join train and features
da_1 = pd.merge(train,features,on = ('Store','Date'),how='left')
da = pd.merge(da_1,stores,on = 'Store',how='left')

da.to_csv('da.csv',index=True)