from gui import *
from PIL import Image
import cv2

class Main:
    def __init__(self):
        MainWindow

    def execute(feature, imageDir, DestDir):
        temp = imageDir.split("/")
        temp2 = temp[-1].rsplit(".",1)
        image_name = temp2[0]
        image_ext = temp2[1]
        if feature == "compress":
            img = Image.open(imageDir)
             # resizing images to given dimension (800x500)
            img = img.resize((800, 500), resample=1)
            img.save(
                os.path.join(DestDir, image_name+"_compress."+image_ext),
                optimize = True,
                # image quality = 70
                quality = 70
            )
        elif feature == "greyscale":
            image = cv2.imread(imageDir)
            # change images to grey
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(DestDir , image_name+"_greyscale."+image_ext), gray_image)
        elif feature == "smoothing":
            image = cv2.imread(imageDir)
            # smoothing image using bilateralfilter
            smooth_image = cv2.bilateralFilter(image,9,75,75)
            cv2.imwrite(os.path.join(DestDir , image_name+"_smoothing."+image_ext), smooth_image)
