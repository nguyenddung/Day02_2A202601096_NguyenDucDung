import pandas as pd
import os
import json
path = r'd:\AI Thuc Chien\Lab\K4-Day02-AI-Product-Labs\nhóm a Lãm.xlsx'
df = pd.read_excel(path, sheet_name='Trang tính1')
print('shape', df.shape)
print('columns', list(df.columns))
print('\n--- first 20 rows ---')
for i, row in df.head(20).iterrows():
    print('ROW', i)
    for c, v in row.items():
        if pd.notna(v) and str(v).strip() != '':
            print(c, '=>', str(v)[:600])
    print('---')
