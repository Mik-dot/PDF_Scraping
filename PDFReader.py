# This project is designed to scrape values from a PDF
# First, packages PANDAS and Tabula-py were installed

import os
import tabula as tb
import pandas as pd

df1 = pd.DataFrame([])
for filename in os.listdir(r'C:\Users\micke\OneDrive\Desktop\Python\pythonProjectPDF\Quotes-Fisher'):

    file = os.path.join(r'C:\Users\micke\OneDrive\Desktop\Python\pythonProjectPDF\Quotes-Fisher', filename)

    df2 = (tb.read_pdf(file, guess=False, multiple_tables=True, pages='all', area=(100, 100, 800, 900), columns=[0,200,450,1000],
                       pandas_options={'header': None}, stream=True))

    df1 = df1.append(df2)


df1 = df1.drop(columns = [2])
df1[['Per Each','Extended']] = df1[3].str.split(" ", 1, expand=True)
df1 = df1.drop(columns = [3, 0])
df1 = df1.dropna()

df1.to_csv(r'C:\Users\micke\OneDrive\Desktop\Python\pythonProjectPDF\Quotes-Fisher\FisherParts.csv')
