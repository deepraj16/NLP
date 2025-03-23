import numpy as np
import pandas as pd

df = pd.read_csv('spam-2.csv')

# drop last 3 cols
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)


