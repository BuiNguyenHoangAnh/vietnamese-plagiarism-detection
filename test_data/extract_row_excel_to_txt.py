
import pandas as pd 

df=pd.read_csv("exact_copy.csv",sep=",")

for index in range(len(df)):
     with open(df["no."][index] +  '.txt', 'w', encoding="utf-8") as output:
        output.write(str(df["document"][index]))