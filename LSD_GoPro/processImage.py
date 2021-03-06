import time
import cv2
import numpy as np
import os

def crop(image):
	return image
	#return image[128:,:]    
	#return image[240:,640:]
    


def process(fileLocation,filename):

	image = cv2.imread(fileLocation+"/"+filename)

	print image.shape

	startConversionTime = time.time()
	rgbImage = cv2.cvtColor(image, cv2.COLOR_YUV2RGB, 3)
	print("RGB conversion time: ",time.time()-startConversionTime)

	startGrayConversionTime = time.time()

	gray_image = cv2.cvtColor(rgbImage, cv2.COLOR_BGR2GRAY)
	print("Gray conversion time: ",time.time()-startGrayConversionTime)
	print("Total conversion time: ",time.time()-startConversionTime)

	gray_image = crop(gray_image)

	print gray_image.shape 
	
	processedLocation = fileLocation+"processed/"
	if not os.path.exists(processedLocation):
    		os.mkdir(processedLocation)

	filename = processedLocation + os.path.basename(filename).rjust(10, '0')
	cv2.imwrite(filename,gray_image)
	print("Total processing time: ",time.time()-startConversionTime)
	print filename
