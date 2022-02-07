import tabula
import sys
# from tabula.io import read_pdf


import pandas as pd
from pdfile3 import pdf_extraction

# df=tabula.read_pdf(r"C:\Users\rdharavath\Downloads\newfile\CoAs SNF France\COA_4139862_1666278103_MAGNAFLOC LT 31.pdf",pdf_extraction(), multiple_tables=True, stream=True)

df = tabula.read_pdf(r"C:\Users\rdharavath\Downloads\newfile\CoAs SNF France\COA_4139862_1666278103_MAGNAFLOC LT 31.pdf",
                pdf_extraction(),columns=pdf_extraction(),stream=True, lattice=True ,guess = True,pages=all, multiple_tables=True)



 

