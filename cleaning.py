import pandas as pd
df = pd.read_csv('Forward_Feast_Survey.csv')
print(df.count()/len(df)*100) 