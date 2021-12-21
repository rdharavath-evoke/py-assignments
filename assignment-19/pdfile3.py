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

def pdf_extraction():
    for page in pages:
        print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        y_axis=[]
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                y, text =lobj.bbox[3], lobj.get_text()
                charecters = ["UNIT","SPECIFICATION"]
                for x in charecters:
                    if x.lower() in text.lower():
                        y_axis.append(int(y))
        y_axis.sort()                
        print(y_axis)  
        print(type(y_axis))          
        converted_list = [str(element) for element in y_axis]
        joined_string = ",".join(converted_list)        
        print(joined_string)
        print(type(joined_string))
        return joined_string
                    
            
            