from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

#path=r"D:\myfiles\tableform.pdf"
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = "1234"
    maxpages = 1
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    text1=text.split()
    numbers=[]
    for item in text1:
        for subitem in item.split():
            if subitem.isdigit() and 100<int(subitem)<9999999999:
                numbers.append(subitem)
    print(numbers)


    fp.close()
    device.close()
    retstr.close()

convert_pdf_to_txt(r"D:\myfiles\tableform.pdf")