from __future__ import division
from math import exp
from numpy import *
import numpy as np
from random import normalvariate
from datetime import datetime
import pandas as pd
import os
current_path = os.path.dirname(__file__)
def getAccuracy(dataMatrix, w_0, w, v,test):
    m, n = shape(dataMatrix)
    ans = []
    #allItem = 0
    mse = 0
    result = []
    #print(m)
    for x in range(m):  
        #allItem += 1
        
        inter_1 = dataMatrix[x] * v
        inter_2 = multiply(dataMatrix[x], dataMatrix[x]) * multiply(v, v)
        interaction = sum(multiply(inter_1, inter_1) - inter_2) / 2.
        p = w_0 + dataMatrix[x] * w + interaction  
        schoolname = test.iloc[x+410,-2]
        majorname = test.iloc[x+410,-1]
        #print(str(p[0,0]) + ' ' + schoolname + ' ' + majorname)
        ans.append([schoolname,majorname,p[0,0]])
    ans.sort(key= lambda x: x[2],reverse = True)
    #print(ans)
    return ans
    

def preprocessData(data): 
    df1 = data
    #print(df1.keys())
    df2=pd.get_dummies(df1)

    feature = np.array(df2)

    #label=np.array(label)

    dataTrain = feature[:410,:]
    dataTest = feature[410:,:]

    return dataTrain,dataTest

def returnSchoolMajor():
    D=np.load(current_path+"/FM_parameter_0.24_withoutNor.npz")
    test = pd.read_excel(current_path+'/new_info.xls',sheet_name = 0)
    dataTrain, dataTest = preprocessData(test)
    ans = getAccuracy(mat(dataTest), D['arr_0'], D['arr_1'], D['arr_2'], test)
    '''
    with open('./result.txt','a+') as f:
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                f.write(str(ans[i][j]) + '||')
            f.write('\n')
    '''

    scores = [i[2] for i in ans]
    le = int((scores[0] - scores[-1]) / len(scores) * 100)
    top = ans
    for i in range(len(top)):
        top[i][2] = 100 - le * i

    # print(top3)
    return top

#print(mse)

#top3 = returnSchoolMajor()
#print(top3)