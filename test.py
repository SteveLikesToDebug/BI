from PIL import Image

try:
    img = Image.open('IMG_2488.png')
    img.show()  # This should open the image in your default image viewer
except IOError:
    print("Error: Cannot open the image.")