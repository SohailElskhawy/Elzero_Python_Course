
# Assigment 3
from PIL import Image

my_image = Image.open(r"C:\Users\sohai\OneDrive\Desktop\All About Programming\Python Projects\Assigments\86_89_Assigments\elzero-pillow.png")
    
# my_image.show()


image1_box = (400,0,800,400)
myCropped1 = my_image.crop(image1_box)
myCropped1 = myCropped1.convert("L")
# myCropped1.save("cropped_L_Letter.png")
myCropped1.show()

image2_box = (0,400,1200,800)
myCropped2 = my_image.crop(image2_box)
myCropped2 = myCropped2.convert("L")
myCropped2 = myCropped2.rotate(180)
# myCropped2.save("croppedImage2.png")
myCropped2.show()

