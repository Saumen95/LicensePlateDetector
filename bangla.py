import cv2
import matplotlib.pyplot as plt
import os
import pytesseract as pt
from PIL import Image, ImageEnhance, ImageFilter
import re

file_path = os.listdir('./images')
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = Image.open('./images/13.jpg')
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(4) # Tried some optimizationpip
im = im.convert('1')
im.save('./images/temp2.png')
bangla_image = cv2.imread('./images/temp2.png') #CONVERT TO GRAY image format
gray_bangla = cv2.cvtColor(bangla_image, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray_bangla,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,85, 11 )
plt.imshow(adaptive_threshold, cmap='gray',vmin=0,vmax=255)
data = pt.image_to_string(adaptive_threshold, lang='eng+ben', config='--psm 6')
print(data)

def format(data):
    regex = ("^(([A-Z]{2}[0-9]{2})" +
             "( )|([A-Z]{2}-[0-9]" +
             "{2}))((19|20)[0-9]" +
             "[0-9])[0-9]{7}$")
    p = re.compile(regex)
    if p == None:
        return False
    if (re.search(p,data)):
        return data
    else:
        return -1
