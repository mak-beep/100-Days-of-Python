from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
import numpy as np


driver = webdriver.Chrome()

URL = "https://www.amazon.com/dp/B09QC3MH4X/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B09QC3MH4X&content-id=amzn1.sym.eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&s=toys-and-games&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"

driver.get(url=URL)

with open('Logo.png', 'wb') as file:
#identify image to be captured
   l = driver.find_element(by=By.CSS_SELECTOR, value=".a-text-center img")
#write file
   file.write(l.screenshot_as_png)

filename = './Logo.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)
print(driver.title)
# To keep page open
while True:
    pass

# import cv2
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# img = cv2.imread('Logo.png')
#
# # Adding custom options
# custom_config = r'--oem 3 --psm 6'
# print(pytesseract.image_to_string(img, config=custom_config))