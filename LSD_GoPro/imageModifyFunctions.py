import glob
import cv2

from processImage import process

fileLocation = "droneImages5"

count = 80
try:

	while count> -1:
		process(fileLocation, "%d.jpg"%count)
		count = count + 1
except AttributeError as ae:
	if(str(ae) == "'NoneType' object has no attribute 'shape'"):
		print("All files have been processed")
	else:
		print(ae)
