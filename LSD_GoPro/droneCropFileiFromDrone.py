import time
import cv2
import numpy as np

def crop(image):
    return image[240:,640:]


def process(image):

        #image = file #cv2.imread(filename)
        print image.shape
'''
   	startConversionTime = time.time()
        rgbImage = cv2.cvtColor(image, cv2.COLOR_YUV2RGB, 3)
        print("RGB conversion time: ",time.time()-startConversionTime)

        startGrayConversionTime = time.time()

        gray_image = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2GRAY)
        print("Gray conversion time: ",time.time()-startGrayConversionTi$
        print("Total conversion time: ",time.time()-startConversionTime)


        print gray_image.shape
'''
   	# cropping the image
        startCropTime = time.time()
        croppedImage = crop(image)
        print("cropping time: ",time.time()-startCropTime)
        print croppedImage.shape

        #filename = 'cropped/'+filename
        #cv2.imwrite(filename,croppedImage)
        #print filename
        return croppedImage

