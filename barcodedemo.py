import barcode 
from barcode.writer import ImageWriter
from PIL import Image

digit = input("Enter the code to generate barcode, needs to an integer : ")

barcode_format = barcode.get_barcode_class('upc')

#barcode and render as image
the_barcode = barcode_format(digit, writer=ImageWriter())

the_barcode.save('generated_barcode')

Image.open('generated_barcode.png')


