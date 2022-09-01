import pywhatkit as kit

from PIL import Image

hand_written = input("Enter text to be handwritten: ")

kit.text_to_handwriting(hand_written, save_to="handwriting.png")

Image.open("handwriting.png")
