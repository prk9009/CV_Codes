import numpy as np
import cv2

cap = cv2.VideoCapture(0)# the number given is the camera u want to use
#if u want to read from a file just put its name there


#cap.get(propId)
#cap.set(propId,val)
#For example, I can check the frame width and height by cap.get(3) and cap.get(4). It gives me 640x480 by
#default. But I want to modify it to 320x240. Just use ret = cap.set(3,320) and ret = cap.set(4,240).

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')#DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size
#video. X264 gives very small size video)

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,180)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Our operations on the frame come here
        # write the flipped frame
        #out.write(frame)
	cv2.imwrite('out.png', frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
