from PIL import Image
import pywhatkit

Image.open("lionpy.jpg")

pywhatkit.image_to_ascii_art("lionpy.jpg", "art")
read_file = open("art.txt", "r")

print(read_file.read())



