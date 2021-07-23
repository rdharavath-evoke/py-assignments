from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
for page_layout in extract_pages(r"D:\myfiles\tableform.pdf"):
    for element in page_layout:
        if isinstance(element,LTTextContainer):
                text=element.get_text()
                text1=text.split()
                numbers=[]
                str=" "
                for item in text1:
                    for subitem in item.split():
                        if subitem.isnumeric() and 100<int(subitem)<9999999999999:
                            numbers.append(subitem)
                            print(numbers)
                