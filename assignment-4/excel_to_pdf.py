import openpyxl
import logging
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


logging.basicConfig(level=logging.DEBUG)

file=r"D:\py-assignments-new\py-assignments\assignment-2\pdfreader.xlsx"
wb=openpyxl.load_workbook(file)
ws=wb.active


for c1,c2,c3 in ws['A1':'C29']:
    logging.debug("    {0:29} {1:29} {2:29}  ".format(c1.value,c2.value,c3.value))

doc=SimpleDocTemplate("simple_table.pdf",pagesizes=letter)

data=pd.ExcelFile(file)

df=data.parse('Sheet1')
vals=df.values
data1=vals.tolist()

elements=[]
t=Table(data1)
elements.append(t)
doc.build(elements)
