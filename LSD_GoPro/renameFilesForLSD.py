import os
import glob
import cv2

print("Start")
count = 0
while count > -1:
	filename =  "{0}{1}".format("droneImagesAll/", os.path.basename("droneImages5/%d.jpg"%count).rjust(10, '0')
	os.rename("droneImagesAllprocessed/%d.jpg"%count, filename)
print("End")
