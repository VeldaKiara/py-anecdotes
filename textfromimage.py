import pytesseract #lib to read text to from image
import cv2 

img = cv2.imread('extractimage.png')
print(pytesseract.image_to_string(img))

cv2.imshow('Result', img)
cv2.waitKey(0)

