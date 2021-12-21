from pdfminer.layout import LAParams, LTTextBox, LTText, LTTextBoxHorizontal
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

fp = open(r"C:\Users\rdharavath\Downloads\newfile\CoAs SNF France\COA_4139862_1666278103_MAGNAFLOC LT 31.pdf", 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)


for page in pages:
    print('Processing next page...')
    interpreter.process_page(page)
    layout = device.get_result()
    text_=input("Enter input  :" )
    
    for lobj in layout:
        if isinstance(lobj, LTTextBox):
            y, text =lobj.bbox[0], lobj.get_text()
            
            if text_=='UNIT':
                if 245.34<=y<=250.74:
                    print(' %s' %  text)
            elif text_=='SPECIFICATION':
                if 300.31<=y<=311.11:
                    print(' %s' %  text)
            elif text_=='QC_TEST':
                if y==517.76:
                    print(' %s' %  text)
        