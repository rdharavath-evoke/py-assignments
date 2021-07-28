from matplotlib.transforms import Bbox
import openpyxl
import logging
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


logging.basicConfig(level=logging.DEBUG)

file=r"D:\py-assignments-new\py-assignments\assignment-2\pdfreader.xlsx"
wb=openpyxl.load_workbook(file)
ws=wb.active


for c1,c2,c3 in ws['A1':'C29']:
    logging.debug("    {0:29} {1:29} {2:29}  ".format(c1.value,c2.value,c3.value))


wb.save(r"D:\py-assignments-new\py-assignments\assignment-2\pdfreader.xlsx")

data=pd.ExcelFile(file)
print(data.sheet_names)
df=data.parse('Sheet1')
print(df.head(10))

fig=plt.subplots(figsize=(12,3))
ax=plt.subplot(111)
ax.axis('off')
the_table=ax.table(cellText=df.values, colLabels=df.columns,bbox=[0,0,1,1])
print(the_table)

pdf.output("excel-pdf.pdf")
