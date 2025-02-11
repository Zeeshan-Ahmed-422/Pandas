import pandas as pd
var=pd.DataFrame({"A":[2,3,4,5,6],"B":[1,2,3,4,5]})
print(var)
print(var)

var.insert(1,"python",[3,4,5,6,7])
var.insert(1,"python_1",var["A"])
var["python1"]=var["A"][:2]

print(var)

var_1=var.pop("python1")
print(var_1)
print(var)