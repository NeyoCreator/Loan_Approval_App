import sys
import cv2
import numpy as np
import pytesseract
from datetime import datetime

startTime = datetime.now()


img = cv2.imread('full_image.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invGamma = 1.0 / 0.3
table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype(
    "uint8"
)

# apply gamma correction using the lookup table
gray = cv2.LUT(gray, table)

ret, thresh1 = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[
    -2:
]


def biggestRectangle(contours):
    biggest = None
    max_area = 0
    indexReturn = -1
    for index in range(len(contours)):
        i = contours[index]
        area = cv2.contourArea(i)
        if area > 100:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.1 * peri, True)
            if area > max_area:  # and len(approx)==4:
                biggest = approx
                max_area = area
                indexReturn = index
    return indexReturn


indexReturn = biggestRectangle(contours)
hull = cv2.convexHull(contours[indexReturn])

# create a crop mask
mask = np.zeros_like(img)  # Create mask where white is what we want, black otherwise
cv2.drawContours(mask, contours, indexReturn, 255, -1)  # Draw filled contour in mask
out = np.zeros_like(img)  # Extract out the object and place into output image
out[mask == 255] = img[mask == 255]

# crop the image
(y, x, _) = np.where(mask == 255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
out = img[topy : bottomy + 1, topx : bottomx + 1, :]


# predict tesseract
lang = "eng+nld"
config = "--psm 11 --oem 3"
out_rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

# uncomment to see raw prediction
# print(pytesseract.image_to_string(out_rgb, lang=lang, config=config))


img_data = pytesseract.image_to_data(
    out_rgb,
    lang=lang,
    config=config,
    output_type=pytesseract.Output.DATAFRAME,
)
img_conf_text = img_data[["conf", "text"]]
img_valid = img_conf_text[img_conf_text["text"].notnull()]
img_words = img_valid[img_valid["text"].str.len() > 1]

# to see confidence of one word
# word = "Gulfaraz"
# print(img_valid[img_valid["text"] == word])

all_predictions = img_words["text"].to_list()
print(all_predictions)

confidence_level = 90

img_conf = img_words[img_words["conf"] > confidence_level]
predictions = img_conf["text"].to_list()

# uncomment to see confident predictions
# print(predictions)

print("Execution Time: {}".format(datetime.now() - startTime))