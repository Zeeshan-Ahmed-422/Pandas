import pandas as pd
x=[2,3,4,5,6]
var=pd.DataFrame(x)
print(var)
print(type(var))

print()


#made with dictionary
d={"a":[1,2,3,3],"b":[4,5,6,7],1:[1,2,3,7]}
# v=pd.DataFrame(d,columns=["a",1],index=["a","s","d","b"])
v=pd.DataFrame(d)
print(v["a"][0])

print(v)

#made with list

list_1=[[2,3,4,5],[1,2,3,4]]
vor=pd.DataFrame(list_1)
print(type(vor))
print(vor)
#made with series
sr={"a":pd.Series([1,2,3,4]),"b":pd.Series([1,2,3,4])}
df=pd.DataFrame(sr)
print(df)

print(type(df))
