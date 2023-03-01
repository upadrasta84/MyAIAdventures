from PIL import Image
import pytesseract
import numpy as np

#install tesseract with pip
#install tesseract windows program from https://github.com/UB-Mannheim/tesseract/wiki

filename = 'download.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)

