# from PIL import Image

# from pytesseract import pytesseract
  
# # Defining paths to tesseract.exe
# # and the image we would be using                                              
# path_to_tesseract = r"C:\Users\rdharavath\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# image_path = r"D:\Solenis\Project\SOLENIS SHANGHAI-NEW2\PO#4533740457\file_seperate_pdf_4.pdf"
  
# # Opening the image & storing it in an image object
# img = Image.open(image_path)
  
# # Providing the tesseract executable
# # location to pytesseract library
# pytesseract.tesseract_cmd = path_to_tesseract
  
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
# text = pytesseract.image_to_string(img)
  
# # Displaying the extracted text
# print(text[:-1])


# from PIL import Image
# import pytesseract

# file = Image.open(r"D:\Solenis\Project\SOLENIS SHANGHAI-NEW2\PO#4533740457\file_seperate_pdf_4.pdf")
# str = pytesseract.image_to_string(file, lang='eng')

# print(str)

# from pdf2image import convert_from_path
# from pytesseract import image_to_string

# def convert_pdf_to_img(pdf_file):
#     return convert_from_path(pdf_file)

# def convert_image_to_text(file):
#     text=image_to_string(file)
#     return text
# def get_text_from_any_pdf(pdf_file):
#     images=convert_pdf_to_img(pdf_file)
#     final_text=""
#     for pg, img in enumerate(images):
#         final_text+=convert_image_to_text(img)
#     return final_text

# path_to_pdf=r"D:\Solenis\Project\SOLENIS SHANGHAI-NEW2\PO#4533740457\file_seperate_pdf_4.pdf"
# print(get_text_from_any_pdf(path_to_pdf))   
    
    
import pytesseract as tess
tess.tessaract_cmd=r"C:\Users\rdharavath\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
from PIL import Image

img=Image.open('r"D:\Solenis\Project\SOLENIS SHANGHAI-NEW2\PO#4533740457\file_seperate_pdf_4.pdf"')
text=tess.image_to_string(img)

print(text)

