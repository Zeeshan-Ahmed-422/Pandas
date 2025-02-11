import pandas as pd
var={"a":[2,3,4,5],"b":[4,5,6,7]}
c=pd.DataFrame(var)
# print(c)
c["d"]=c["a"]-c["b"]
c["e"]=c["a"]*c["b"]
c["f"]=c["a"]/c["b"]
c["game"]=c["a"]<=4

var_1={"a":[20,30,40,50],"b":[14,15,16,17]}
d=pd.DataFrame(var_1)
# print(d)
d["python"]=d["a"]<=30
print(d)

print(c)