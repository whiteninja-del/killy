import pandas as pd
from openpyxl import load_workbook

wb=load_workbook("tree2.gnumeric")
#get the first sheet
sheet=wb.active
#convert to pandas dataframe
data=sheet.values
cols=next(data)[0:]
df=pd.DataFrame(data, columns=cols)
print(df)
