import pandas as pd

x=[3,4,5,6,7]
var=pd.Series(x,index=['a','b','c','d','e'],dtype=float,name="python")
print(var)
print(type(var))
# print(var[2])
dic={"name:":["python","c","c++"],"age :":["2","3","4"]}
var1=pd.Series(dic)
print(var1)

s=pd.Series(12,index=[1,2,3,4,5,6])
# print(s)
v=pd.Series(12,index=[1,2,3])
a=s+v 
print(a)
