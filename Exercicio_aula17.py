import pandas as pd

df1 = pd.read_csv(r"C:\Users\deadp\OneDrive\Textos, roteiros e sinopses\VS studio\funcionarios.csv")

df2 = pd.read_csv(r"C:\Users\deadp\OneDrive\Textos, roteiros e sinopses\VS studio\funcionarios - Null.csv")

""" print(df1)

print("\n")

print(df2)
 """

df_somada = pd.concat([df1, df2])

print(df_somada)