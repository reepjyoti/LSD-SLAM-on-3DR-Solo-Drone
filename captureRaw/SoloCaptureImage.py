import cv2
import sys
import time
import threading
from SoloCamera import SoloCamera


def crop(image):
	#return image
	return image[128:,:]   


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
                '''
                startReadingTime = time.time()
                image = cv2.imread(frame,0)
                print("image reading time: ",time.time()-startReadingTime)

                startConversionTime = time.time()
                rgbImage = cv2.cvtColor(imgFrame, cv2.COLOR_YUV2RGB, 3)
                print("RGB conversion time: ",time.time()-startConversionTime)

                startGrayConversionTime = time.time()
                gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                print("Gray conversion time: ",time.time()-startGrayConversionTime)
                print("Total conversion time: ",time.time()-startConversionTime)
                '''
                print("before cropping shape: ",frame.shape)
                cropStart = time.time()
                frame = crop(frame)
                print("time to crop image", time.time()-cropStart)
                print(frame.shape)
                fileName = ("%d"% count).rjust(10, '0')
                writeStart = time.time()
                #cv2.imwrite("images/%d.jpg"% count, frame)
                frame.tofile("images/%s"% fileName)
                print("time to write image", time.time()-writeStart)


                count = count + 1

        else:
            print "failed to open gopro"

print ("closing camera...")

