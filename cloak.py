import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(3)
count = 0
background=0

for i in range(60):
	ret,background = cap.read()

while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
                break
	count+=1
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Mask to detect red color
	lower_red = np.array([0, 100, 100])
	upper_red = np.array([10, 255, 255])
	mask1 = cv2.inRange(hsv,lower_red,upper_red)

	lower_red = np.array([160,100,100])
	upper_red = np.array([179,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask1 = mask1+mask2

	# Refining the mask corresponding to the detected red color
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2 = cv2.bitwise_not(mask1)

	# Generating the final output
	res1 = cv2.bitwise_and(background,background,mask=mask1)
	res2 = cv2.bitwise_and(img,img,mask=mask2)
	final_output = cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow('Magic !!!',final_output)
	k = cv2.waitKey(10)
	if k == 27:
                break
