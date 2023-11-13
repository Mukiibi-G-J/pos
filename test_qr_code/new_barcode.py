from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image

# Generate the barcode image
ean = Code128('123456789', writer=ImageWriter())

# Save the barcode image as a PNG file
filename = ean.save('mybarcode')

# Open the generated image
barcode_image = Image.open('mybarcode.png')

# Define the new size (width, height)
new_size = (100, 100)  # Adjust as needed

# Resize the image with antialiasing
barcode_image = barcode_image.resize(new_size, Image.LANCZOS)

# Save the resized image
barcode_image.save('mybarcode_resized.png')

# Optional: You can also overwrite the original image with the resized one if needed
barcode_image.save('mybarcode.png')

# Close the image
barcode_image.close()
