# from PIL import Image
# import pytesseract

# path_of_image = 'extractimage.png'
# img = Image.open(path_of_image)
# text = pytesseract.image_to_string(img)


import pytesseract
import cv2

img = cv2.imread('extractimage.png')
print(pytesseract.image_to_string(img))

cv2.imshow('Result', img)
cv2.waitKey(0)
