import cv2
import time
import numpy as np
import glob
from PIL import Image
import os

filePath =  "droneImagesRsync/images/"
print(filePath)
for filename in sorted(glob.iglob(filePath+'*')):
	starttime = time.time()
	fd = open(filename)

	f= np.fromfile(fd,dtype=np.uint8)
	fshape = f.reshape((592,1280))
	print("getting images: ",time.time()-starttime)

	writeStart = time.time()
	im = Image.fromarray(fshape)
	im.save("processedDrone/"+os.path.basename(filename)+".jpg")
	#cv2.imwrite("images/%d.jpg"% count, frame)
	#gray_image.tofile("%d".rjust(10, '0')% count)		
	print("time to write image", time.time()-writeStart)

	
