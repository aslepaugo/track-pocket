#pip install pytesseract

from PIL import Image
import pytesseract

print("Hi")

img = Image.open("IMG_5723.JPG")
#print(pytesseract.get_languages(config=''))

text = pytesseract.image_to_string(img)

print(text)
