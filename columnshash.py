import pandas as pd
import hashlib

def hash_column(column):
    return column.apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())


df = pd.read_csv('Caminho do arquivo',sep=';')
print(df.head())
for column in df.columns:
        print(column)

df=df.drop(columns=["coluna1",'coluna2','coluna3'])

columns_to_hash = ['colunaA', 'colunaB']

for col in columns_to_hash:
    if col in df.columns:
        df[col] = hash_column(df[col])


output_file_path = 'caminho do arquivo/nome do arquivo.csv'
df.to_csv(output_file_path, index=False,sep=';')