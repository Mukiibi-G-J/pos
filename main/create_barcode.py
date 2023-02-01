
from barcode import Code128
from barcode.writer import ImageWriter
import uuid
import pathlib
import os 


url = pathlib.Path(__file__).parent.absolute()
# first check if the directory exists
if not os.path.exists('images'):
    # if not, create it
    images_dir = os.mkdir('images')

number = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
]

for i in number:
    code = uuid.uuid4()
    code = str(code).replace('-', '')[:14]
    barcode = Code128(code, writer=ImageWriter())
    # save the barcode to a file in the images directory
    barcode.save(f'images/{code}')