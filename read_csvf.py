import pandas as pd
# a=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv")
# print(a)

b=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",nrows=1)
print(b)
# c=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",usecols=["Age","Gender"])
# print(c)
# d=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",usecols=[0,2])
# print(d)
# e=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",skiprows=[0])
# print(e)
# f=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",index_col=["Gender"])
# print(f)
# f=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",header=[2])
# print(f)
# g=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",names=["col","col1","col2","col3"])
# print(g)
# h=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",header=None)
# print(h)
# print(type(b))

i=pd.read_csv("D:\\Python\\pandas_practice\\lung_cancer_prediction.csv",dtype={"Age":"float"})
print(i)