import cv2
import sys
import time
import threading
from SoloCamera import SoloCamera


#open HDMI-In as a video capture device
#BE SURE YOU HAVE RUN `SOLO VIDEO ACQUIRE`
cam = SoloCamera()
count = 0
while count > -1:
	if cam.isOpened():
	    print "Capturing an image..."
	    startTime= time.time()
	    ret, frame = cam.read()
	    print("time to read camera",time.time()-startTime)
	    if frame is None:
	        print "No image"
	    else:
		#frame = cv2.imread(frame)
		writeStart = time.time()
        	cv2.imwrite("images/%d.jpg"% count, frame)
		count = count + 1
		print("time to write image", time.time()-writeStart)
	else:
	    print "failed to open gopro"
 	
print ("closing camera...")
