import paramiko
from scp import SCPClient
import os.path
import time

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.1.1.10", username="root", password="TjSDBkAu")
print("Connected")

scp = SCPClient(ssh.get_transport())
count = 0

while count > -1:
		#if(os.path.isfile("~/captureImage/images/%d.jpg'%count")):
	
	try:
		fileName = ("%d"% count).rjust(10, '0')+".jpg"
		copySartTime= time.time()	
		scp.get(r'~/captureImage/images/%s'%fileName, r'/home/reepjyoti/sem_project/LSD_GoPro/droneImages/%s'%fileName)
		print("time to copy image",time.time()-copySartTime)
		count = count + 1
	
	except AttributeError:
	
		scp.close()
		print("Number of Files Copied: %d"%count)
		print(AttributeError) 
	except: 
		count = count + 1
		print (count)
		time.sleep(4)

