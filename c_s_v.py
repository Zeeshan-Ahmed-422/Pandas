import pandas as pd
a={"a":[2,3,4],"b":[5,6,7]}
s=pd.DataFrame(a)
print(s)
# s.to_csv("Test_new.csv")
# s.to_csv("Test_new2.csv",index=False,header=[1,2,3])
s.to_csv("Test_new2.csv",index=False,header=[1,2])