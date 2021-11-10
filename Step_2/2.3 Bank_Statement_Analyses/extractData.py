# Aim :to extract data from the image bank statement

#importing the libraries
import cv2
import numpy as np
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

#create a function that wwill return a threshold image and the value 
def extract_data(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshed = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,17)
    text1 = tess.image_to_data(threshed,output_type='data.frame')
    text2 = tess.image_to_string(threshed)
    text = text1[text1.conf != -1]
    # lines = text.groupby('block_num')['text'].apply(list)
    # conf = text.groupby(['block_num'])['conf'].mean()
    return text2

# implement the function 
img = cv2.imread("page0.jpg")
txt_value = extract_data(img)

# split the string to array
arrValue = txt_value.split("\n")

##print(arrValue[2])