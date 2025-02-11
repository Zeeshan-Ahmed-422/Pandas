import pandas as pd
import numpy as np
c=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv")
# print(c)
# print(c.index)
# print(c.columns)
# print(c.describe())
# print(c.head())
# print(c.tail(2))
# print(c[0:5])  #selective row
# print(c.index.array)
# print(c.to_numpy())
#another method
# a=np.asarray(c)
# print(a)
# print(c.sort_index(axis=0,ascending=False))
# c["Country"][0]="python"
# print(c)
# d=c.loc[1,"Country"]="okhogya"
# print(c)
e=c.loc[[1,3],["Country","Gender"]]
print(e)