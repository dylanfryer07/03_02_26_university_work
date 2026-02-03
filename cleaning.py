import pandas as pd
df = pd.read_csv('Forward_Feast_Survey.csv')
print(df.count()/len(df)*100) 

## Dropping column "4b1. And are you satisfied with what you have?" as on 15% of data is there
df = df.drop(columns='4b1. And are you satisfied with what you have?')
